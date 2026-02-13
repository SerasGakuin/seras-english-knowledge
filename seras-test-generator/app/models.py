"""Domain models, API models, and custom exceptions."""

from dataclasses import dataclass

from fastapi import HTTPException
from pydantic import BaseModel


# --- Domain Models (frozen dataclass) ---


@dataclass(frozen=True)
class CheckPoint:
    question: str
    answer: str


@dataclass(frozen=True)
class KnowledgeNode:
    id: str
    name: str
    category: str
    priority: str  # "P1" / "P2" / "P3"
    prerequisites: tuple[str, ...]
    understanding_goals: tuple[str, ...]
    check_points: tuple[CheckPoint, ...]
    references: dict[str, dict[str, str]]
    notes: str


@dataclass(frozen=True)
class Sentence:
    id: str
    drill: int
    number: int
    role: str  # "example" / "practice"
    english: str
    japanese: str
    structure: dict[str, str]
    knowledge_tags: tuple[str, ...]
    notes: str


@dataclass(frozen=True)
class SectionMapping:
    id: str
    title: str
    pages: str
    type: str  # "introduction" / "drill" / "exam"
    knowledge_nodes: tuple[str, ...]
    prerequisites: tuple[str, ...]
    sentence_file: str | None
    book: str = ""


# --- Output Models ---


@dataclass(frozen=True)
class WarmupQuestion:
    number: int
    question: str
    answer: str
    node_id: str
    node_name: str
    reference_pages: str
    note: str


@dataclass(frozen=True)
class KnowledgeQuestion:
    number: int
    question: str
    answer: str
    node_id: str
    node_name: str
    reference_pages: str


@dataclass(frozen=True)
class SentenceQuestion:
    number: int
    english: str
    japanese: str
    structure: str  # "全体" value
    notes: str
    knowledge_tags: tuple[str, ...]
    focus_points: tuple[str, ...]
    source_pages: str
    source_section: str


@dataclass(frozen=True)
class ReviewGuide:
    node_id: str
    node_name: str
    reference_pages: str
    reason: str


@dataclass(frozen=True)
class NodeSection:
    section_number: int
    node_id: str
    node_name: str
    reference_pages: str
    knowledge_questions: list[KnowledgeQuestion]
    sentence_questions: list[SentenceQuestion]
    review_guide: list[ReviewGuide]


@dataclass(frozen=True)
class TestData:
    sections: list[str]
    sections_label: str
    warmup_questions: list[WarmupQuestion]
    node_sections: list[NodeSection]
    generated_at: str
    book_name: str = ""


# --- API Models (Pydantic) ---


class GenerateTestRequest(BaseModel):
    sections: str  # "1-1~1-5"
    book: str = "hajime"


class TestMetadata(BaseModel):
    sections: list[str]
    knowledge_nodes_used: list[str]
    question_count: int
    sentence_count: int
    warmup_count: int
    generated_at: str
    book: str = ""
    book_name: str = ""


class GenerateTestResponse(BaseModel):
    pdf_url: str
    metadata: TestMetadata


# --- Custom Exceptions ---


class SectionNotFoundError(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=400, detail=detail)


class InvalidSectionRangeError(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=400, detail=detail)


class DataLoadError(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=500, detail=detail)


class DriveUploadError(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=502, detail=detail)
