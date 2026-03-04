"""YAML book data loader."""

from __future__ import annotations

from pathlib import Path

import yaml

from .types import BookData


class YamlBookLoader:
    """Load a book's YAML data directory into a BookData container."""

    def __init__(self, data_dir: str | Path) -> None:
        self.data_dir = Path(data_dir)

    def load(self) -> BookData:
        sections_file = self.data_dir / "sections.yaml"
        if not sections_file.exists():
            raise FileNotFoundError(f"sections.yaml not found in {self.data_dir}")

        sections_data = self._load_yaml(sections_file)
        sections = sections_data.get("sections", [])
        section_knowledge_nodes = sections_data.get("section_knowledge_nodes", [])
        section_prerequisites = sections_data.get("section_prerequisites", [])
        # Normalize variant key names to match DB columns
        for sp in section_prerequisites:
            if "prerequisite_section_id" in sp and "prerequisite_id" not in sp:
                sp["prerequisite_id"] = sp.pop("prerequisite_section_id")

        book_name = sections[0]["book"] if sections else ""

        nodes, goals, checks, prereqs, refs = self._load_knowledge_data()
        sentences, structures, tags = self._load_sentence_data()

        return BookData(
            book_name=book_name,
            knowledge_nodes=nodes,
            understanding_goals=goals,
            check_points=checks,
            node_prerequisites=prereqs,
            knowledge_references=refs,
            sections=sections,
            section_knowledge_nodes=section_knowledge_nodes,
            section_prerequisites=section_prerequisites,
            sentences=sentences,
            sentence_structures=structures,
            sentence_knowledge_tags=tags,
        )

    def _load_knowledge_data(
        self,
    ) -> tuple[list[dict], list[dict], list[dict], list[dict], list[dict]]:
        kn_dir = self.data_dir / "knowledge_nodes"
        nodes: list[dict] = []
        goals: list[dict] = []
        checks: list[dict] = []
        prereqs: list[dict] = []
        refs: list[dict] = []

        if not kn_dir.exists():
            return nodes, goals, checks, prereqs, refs

        for f in sorted(kn_dir.glob("*.yaml")):
            data = self._load_yaml(f)
            if data is None:
                continue
            nodes.extend(data.get("knowledge_nodes", []))
            goals.extend(data.get("understanding_goals", []))
            checks.extend(data.get("check_points", []))
            prereqs.extend(data.get("node_prerequisites", []))
            refs.extend(data.get("knowledge_references", []))

        return nodes, goals, checks, prereqs, refs

    def _load_sentence_data(
        self,
    ) -> tuple[list[dict], list[dict], list[dict]]:
        sn_dir = self.data_dir / "sentences"
        sentences: list[dict] = []
        structures: list[dict] = []
        tags: list[dict] = []

        if not sn_dir.exists():
            return sentences, structures, tags

        for f in sorted(sn_dir.glob("*.yaml")):
            data = self._load_yaml(f)
            if data is None:
                continue
            sentences.extend(data.get("sentences", []))
            structures.extend(data.get("sentence_structures", []))
            tags.extend(data.get("sentence_knowledge_tags", []))

        return sentences, structures, tags

    @staticmethod
    def _load_yaml(path: Path) -> dict | None:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
