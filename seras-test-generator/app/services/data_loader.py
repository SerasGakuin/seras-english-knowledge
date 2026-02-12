"""YAML data loader with in-memory cache."""

from functools import lru_cache
from pathlib import Path

import yaml

from app.models import (
    CheckPoint,
    DataLoadError,
    KnowledgeNode,
    SectionMapping,
    Sentence,
)


def _parse_check_point(raw_cp: dict[str, str]) -> CheckPoint:
    if "question" in raw_cp:
        return CheckPoint(question=raw_cp["question"], answer=raw_cp.get("answer", ""))
    if "assessment" in raw_cp:
        return CheckPoint(question=raw_cp["assessment"], answer="")
    raise DataLoadError(detail=f"Unknown check_point format: {raw_cp}")


class DataStore:
    """Loads and caches all YAML data at initialization."""

    def __init__(self, data_dir: Path) -> None:
        self._data_dir = data_dir
        self._nodes: dict[str, KnowledgeNode] = {}
        self._sections: dict[str, SectionMapping] = {}
        self._sentences: dict[str, list[Sentence]] = {}
        self._load_all()

    def _load_all(self) -> None:
        self._load_knowledge_nodes()
        self._load_mappings()
        self._load_sentences()

    def _load_knowledge_nodes(self) -> None:
        knowledge_dir = self._data_dir / "knowledge"
        if not knowledge_dir.exists():
            return
        for path in sorted(knowledge_dir.rglob("*.yaml")):
            try:
                with open(path, encoding="utf-8") as f:
                    raw = yaml.safe_load(f)
                if not raw or "id" not in raw:
                    continue
                node = KnowledgeNode(
                    id=raw["id"],
                    name=raw["name"],
                    category=raw.get("category", ""),
                    priority=raw.get("priority", "P3"),
                    prerequisites=tuple(raw.get("prerequisites") or []),
                    understanding_goals=tuple(raw.get("understanding_goals") or []),
                    check_points=tuple(
                        _parse_check_point(cp)
                        for cp in (raw.get("check_points") or [])
                    ),
                    references=raw.get("references") or {},
                    notes=raw.get("notes", ""),
                )
                self._nodes[node.id] = node
            except (yaml.YAMLError, KeyError) as e:
                raise DataLoadError(
                    detail=f"Failed to load knowledge node {path}: {e}"
                ) from e

    def _load_mappings(self) -> None:
        mappings_dir = self._data_dir / "mappings"
        if not mappings_dir.exists():
            return
        for path in sorted(mappings_dir.rglob("*.yaml")):
            try:
                with open(path, encoding="utf-8") as f:
                    raw = yaml.safe_load(f)
                if not raw:
                    continue
                for section in raw.get("sections", []):
                    mapping = SectionMapping(
                        id=section["id"],
                        title=section.get("title", ""),
                        pages=section.get("pages", ""),
                        type=section.get("type", "drill"),
                        knowledge_nodes=tuple(
                            section.get("knowledge_nodes") or []
                        ),
                        prerequisites=tuple(
                            section.get("prerequisites") or []
                        ),
                        sentence_file=section.get("sentence_file"),
                    )
                    self._sections[mapping.id] = mapping
            except (yaml.YAMLError, KeyError) as e:
                raise DataLoadError(
                    detail=f"Failed to load mapping {path}: {e}"
                ) from e

    def _load_sentences(self) -> None:
        sentences_dir = self._data_dir / "sentences"
        if not sentences_dir.exists():
            return
        for path in sorted(sentences_dir.rglob("*.yaml")):
            try:
                with open(path, encoding="utf-8") as f:
                    raw = yaml.safe_load(f)
                if not raw:
                    continue
                source = raw.get("source", {})
                section_id = source.get("section", path.stem)
                sentence_list: list[Sentence] = []
                for s in raw.get("sentences", []):
                    sentence = Sentence(
                        id=s["id"],
                        drill=s.get("drill", 0),
                        number=s.get("number", 0),
                        role=s.get("role", "practice"),
                        english=s["english"],
                        japanese=s["japanese"],
                        structure=s.get("structure") or {},
                        knowledge_tags=tuple(s.get("knowledge_tags") or []),
                        notes=s.get("notes", ""),
                    )
                    sentence_list.append(sentence)
                self._sentences[section_id] = sentence_list
            except (yaml.YAMLError, KeyError) as e:
                raise DataLoadError(
                    detail=f"Failed to load sentences {path}: {e}"
                ) from e

    def get_node(self, node_id: str) -> KnowledgeNode | None:
        return self._nodes.get(node_id)

    def get_section(self, section_id: str) -> SectionMapping | None:
        return self._sections.get(section_id)

    def get_sentences(self, section_id: str) -> list[Sentence]:
        return self._sentences.get(section_id, [])

    def get_all_section_ids(self) -> list[str]:
        return sorted(self._sections.keys())

    def section_exists(self, section_id: str) -> bool:
        return section_id in self._sections


@lru_cache(maxsize=1)
def get_data_store() -> DataStore:
    from app.config import get_settings

    return DataStore(Path(get_settings().data_dir))
