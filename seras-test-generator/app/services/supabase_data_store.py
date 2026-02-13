"""Supabase-backed data store (same interface as DataStore)."""

from supabase import Client

from app.models import (
    CheckPoint,
    DataLoadError,
    KnowledgeNode,
    SectionMapping,
    Sentence,
)


class SupabaseDataStore:
    """Loads data from Supabase PostgreSQL via REST API."""

    def __init__(self, client: Client) -> None:
        self._client = client

    def get_node(self, node_id: str) -> KnowledgeNode | None:
        """Fetch a single knowledge node with all related data."""
        try:
            row = (
                self._client.table("knowledge_nodes")
                .select("*")
                .eq("id", node_id)
                .maybe_single()
                .execute()
            )
            if row is None or row.data is None:
                return None

            node_data = row.data

            # Prerequisites
            prereqs = (
                self._client.table("knowledge_node_prerequisites")
                .select("prerequisite_id")
                .eq("node_id", node_id)
                .execute()
            )
            prerequisites = tuple(r["prerequisite_id"] for r in prereqs.data)

            # Understanding goals (ordered by seq)
            goals = (
                self._client.table("understanding_goals")
                .select("goal")
                .eq("node_id", node_id)
                .order("seq")
                .execute()
            )
            understanding_goals = tuple(r["goal"] for r in goals.data)

            # Check points (ordered by seq)
            cps = (
                self._client.table("check_points")
                .select("question, answer")
                .eq("node_id", node_id)
                .order("seq")
                .execute()
            )
            check_points = tuple(
                CheckPoint(question=r["question"], answer=r.get("answer", ""))
                for r in cps.data
            )

            # References: build dict[book, dict[section_id, pages]]
            refs = (
                self._client.table("knowledge_references")
                .select("book, section_id, pages")
                .eq("node_id", node_id)
                .execute()
            )
            references: dict[str, dict[str, str]] = {}
            for r in refs.data:
                book = r["book"]
                if book not in references:
                    references[book] = {}
                references[book][r["section_id"]] = r["pages"]

            return KnowledgeNode(
                id=node_data["id"],
                name=node_data["name"],
                category=node_data.get("category", ""),
                priority=node_data.get("priority", "P3"),
                prerequisites=prerequisites,
                understanding_goals=understanding_goals,
                check_points=check_points,
                references=references,
                notes=node_data.get("notes", "") or "",
            )
        except Exception as e:
            if isinstance(e, DataLoadError):
                raise
            raise DataLoadError(
                detail=f"Failed to load knowledge node {node_id}: {e}"
            ) from e

    def get_section(self, section_id: str) -> SectionMapping | None:
        """Fetch a single section mapping with related data."""
        try:
            row = (
                self._client.table("sections")
                .select("*")
                .eq("id", section_id)
                .maybe_single()
                .execute()
            )
            if row is None or row.data is None:
                return None

            section_data = row.data

            # Knowledge nodes (ordered by seq)
            kn = (
                self._client.table("section_knowledge_nodes")
                .select("node_id")
                .eq("section_id", section_id)
                .order("seq")
                .execute()
            )
            knowledge_nodes = tuple(r["node_id"] for r in kn.data)

            # Prerequisites
            prereqs = (
                self._client.table("section_prerequisites")
                .select("prerequisite_id")
                .eq("section_id", section_id)
                .execute()
            )
            prerequisites = tuple(r["prerequisite_id"] for r in prereqs.data)

            return SectionMapping(
                id=section_data["id"],
                title=section_data.get("title", ""),
                pages=section_data.get("pages", ""),
                type=section_data.get("type", "drill"),
                knowledge_nodes=knowledge_nodes,
                prerequisites=prerequisites,
                sentence_file=None,  # Not stored in DB
            )
        except Exception as e:
            if isinstance(e, DataLoadError):
                raise
            raise DataLoadError(
                detail=f"Failed to load section {section_id}: {e}"
            ) from e

    def get_sentences(self, section_id: str) -> list[Sentence]:
        """Fetch all sentences for a section with structures and tags."""
        try:
            rows = (
                self._client.table("sentences")
                .select("*")
                .eq("section_id", section_id)
                .order("drill")
                .order("number")
                .execute()
            )
            if not rows.data:
                return []

            sentence_ids = [r["id"] for r in rows.data]

            # Batch-fetch structures for all sentences in this section
            structs = (
                self._client.table("sentence_structures")
                .select("sentence_id, label, value")
                .in_("sentence_id", sentence_ids)
                .execute()
            )
            struct_map: dict[str, dict[str, str]] = {}
            for s in structs.data:
                sid = s["sentence_id"]
                if sid not in struct_map:
                    struct_map[sid] = {}
                struct_map[sid][s["label"]] = s["value"]

            # Batch-fetch knowledge tags for all sentences in this section
            tags = (
                self._client.table("sentence_knowledge_tags")
                .select("sentence_id, node_id")
                .in_("sentence_id", sentence_ids)
                .execute()
            )
            tag_map: dict[str, list[str]] = {}
            for t in tags.data:
                sid = t["sentence_id"]
                if sid not in tag_map:
                    tag_map[sid] = []
                tag_map[sid].append(t["node_id"])

            result: list[Sentence] = []
            for r in rows.data:
                sid = r["id"]
                sentence = Sentence(
                    id=sid,
                    drill=r.get("drill", 0),
                    number=r.get("number", 0),
                    role=r.get("role", "practice"),
                    english=r["english"],
                    japanese=r["japanese"],
                    structure=struct_map.get(sid, {}),
                    knowledge_tags=tuple(tag_map.get(sid, [])),
                    notes=r.get("notes", "") or "",
                )
                result.append(sentence)

            return result
        except Exception as e:
            if isinstance(e, DataLoadError):
                raise
            raise DataLoadError(
                detail=f"Failed to load sentences for {section_id}: {e}"
            ) from e

    def get_all_section_ids(self) -> list[str]:
        """Fetch all section IDs, sorted."""
        try:
            rows = (
                self._client.table("sections")
                .select("id")
                .order("id")
                .execute()
            )
            return [r["id"] for r in rows.data]
        except Exception as e:
            if isinstance(e, DataLoadError):
                raise
            raise DataLoadError(
                detail=f"Failed to load section IDs: {e}"
            ) from e

    def section_exists(self, section_id: str) -> bool:
        """Check if a section exists."""
        try:
            row = (
                self._client.table("sections")
                .select("id")
                .eq("id", section_id)
                .maybe_single()
                .execute()
            )
            return row is not None and row.data is not None
        except Exception as e:
            if isinstance(e, DataLoadError):
                raise
            raise DataLoadError(
                detail=f"Failed to check section existence {section_id}: {e}"
            ) from e
