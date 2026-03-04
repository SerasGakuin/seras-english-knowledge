"""Pre-insert validation for BookData (no DB required)."""

from __future__ import annotations

from .types import BookData, ValidationError


class ImportValidator:
    """Validate a BookData for consistency before DB operations."""

    def validate(self, data: BookData) -> list[ValidationError]:
        errors: list[ValidationError] = []

        # Empty data checks
        if not data.book_name:
            errors.append(ValidationError("book_name", "book_name is empty"))
        if not data.knowledge_nodes:
            errors.append(ValidationError("knowledge_nodes", "knowledge_nodes is empty"))
        if not data.sections:
            errors.append(ValidationError("sections", "sections is empty"))

        # Build ID sets
        node_ids = [n["id"] for n in data.knowledge_nodes]
        section_ids = [s["id"] for s in data.sections]
        sentence_ids = [s["id"] for s in data.sentences]

        # Duplicate ID checks
        self._check_duplicates(errors, "knowledge_nodes", node_ids)
        self._check_duplicates(errors, "sections", section_ids)
        self._check_duplicates(errors, "sentences", sentence_ids)

        node_id_set = set(node_ids)
        section_id_set = set(section_ids)
        sentence_id_set = set(sentence_ids)

        # FK checks: understanding_goals → nodes
        for g in data.understanding_goals:
            if g["node_id"] not in node_id_set:
                errors.append(ValidationError(
                    "understanding_goals",
                    f"references missing node: {g['node_id']}",
                ))

        # FK checks: check_points → nodes
        for c in data.check_points:
            if c["node_id"] not in node_id_set:
                errors.append(ValidationError(
                    "check_points",
                    f"references missing node: {c['node_id']}",
                ))

        # FK checks: node_prerequisites → nodes (both sides)
        for p in data.node_prerequisites:
            if p["node_id"] not in node_id_set:
                errors.append(ValidationError(
                    "knowledge_node_prerequisites",
                    f"references missing node: {p['node_id']}",
                ))
            if p["prerequisite_id"] not in node_id_set:
                errors.append(ValidationError(
                    "knowledge_node_prerequisites",
                    f"references missing prerequisite node: {p['prerequisite_id']}",
                ))

        # FK checks: knowledge_references → nodes
        for r in data.knowledge_references:
            if r["node_id"] not in node_id_set:
                errors.append(ValidationError(
                    "knowledge_references",
                    f"references missing node: {r['node_id']}",
                ))

        # FK checks: section_knowledge_nodes → sections, nodes
        for skn in data.section_knowledge_nodes:
            if skn["section_id"] not in section_id_set:
                errors.append(ValidationError(
                    "section_knowledge_nodes",
                    f"references missing section: {skn['section_id']}",
                ))
            if skn["node_id"] not in node_id_set:
                errors.append(ValidationError(
                    "section_knowledge_nodes",
                    f"references missing node: {skn['node_id']}",
                ))

        # FK checks: section_prerequisites → sections (both sides)
        for sp in data.section_prerequisites:
            if sp["section_id"] not in section_id_set:
                errors.append(ValidationError(
                    "section_prerequisites",
                    f"references missing section: {sp['section_id']}",
                ))
            if sp["prerequisite_id"] not in section_id_set:
                errors.append(ValidationError(
                    "section_prerequisites",
                    f"references missing prerequisite section: {sp['prerequisite_id']}",
                ))

        # FK checks: sentences → sections
        for s in data.sentences:
            if s["section_id"] not in section_id_set:
                errors.append(ValidationError(
                    "sentences",
                    f"sentence {s['id']} references missing section: {s['section_id']}",
                ))

        # FK checks: sentence_structures → sentences
        for st in data.sentence_structures:
            if st["sentence_id"] not in sentence_id_set:
                errors.append(ValidationError(
                    "sentence_structures",
                    f"references missing sentence: {st['sentence_id']}",
                ))

        # FK checks: sentence_knowledge_tags → sentences, nodes
        for t in data.sentence_knowledge_tags:
            if t["sentence_id"] not in sentence_id_set:
                errors.append(ValidationError(
                    "sentence_knowledge_tags",
                    f"references missing sentence: {t['sentence_id']}",
                ))
            if t["node_id"] not in node_id_set:
                errors.append(ValidationError(
                    "sentence_knowledge_tags",
                    f"references missing node: {t['node_id']}",
                ))

        return errors

    @staticmethod
    def _check_duplicates(
        errors: list[ValidationError], table: str, ids: list[str]
    ) -> None:
        seen: set[str] = set()
        dupes: set[str] = set()
        for id_ in ids:
            if id_ in seen:
                dupes.add(id_)
            seen.add(id_)
        if dupes:
            errors.append(ValidationError(
                table, f"duplicate IDs: {sorted(dupes)}"
            ))
