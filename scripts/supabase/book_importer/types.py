"""Data types for the book importer."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ValidationError:
    """A single validation error."""

    table: str
    message: str

    def __str__(self) -> str:
        return f"[{self.table}] {self.message}"


@dataclass
class BookData:
    """Container for one book's complete dataset."""

    book_name: str
    knowledge_nodes: list[dict] = field(default_factory=list)
    understanding_goals: list[dict] = field(default_factory=list)
    check_points: list[dict] = field(default_factory=list)
    node_prerequisites: list[dict] = field(default_factory=list)
    knowledge_references: list[dict] = field(default_factory=list)
    sections: list[dict] = field(default_factory=list)
    section_knowledge_nodes: list[dict] = field(default_factory=list)
    section_prerequisites: list[dict] = field(default_factory=list)
    sentences: list[dict] = field(default_factory=list)
    sentence_structures: list[dict] = field(default_factory=list)
    sentence_knowledge_tags: list[dict] = field(default_factory=list)


@dataclass
class ImportResult:
    """Result of an import run."""

    success: bool
    book_name: str
    errors: list[ValidationError] = field(default_factory=list)
    loaded: dict[str, int] = field(default_factory=dict)
    deleted: dict[str, int] = field(default_factory=dict)
    inserted: dict[str, int] = field(default_factory=dict)
