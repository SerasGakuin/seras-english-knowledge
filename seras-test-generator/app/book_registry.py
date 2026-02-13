"""Book registry: slug -> BookConfig mapping."""

from dataclasses import dataclass

from fastapi import HTTPException


class BookNotFoundError(HTTPException):
    def __init__(self, slug: str) -> None:
        super().__init__(
            status_code=400,
            detail=f"Unknown book: '{slug}'. Available: {', '.join(BOOKS.keys())}",
        )


@dataclass(frozen=True)
class BookConfig:
    slug: str  # "hajime", "hijii"
    full_name: str  # "はじめの英文読解ドリル"
    db_book_name: str  # sections.book column value
    section_prefix: str  # "Ch", "Hij"


BOOKS: dict[str, BookConfig] = {
    "hajime": BookConfig(
        slug="hajime",
        full_name="はじめの英文読解ドリル",
        db_book_name="はじめの英文読解ドリル",
        section_prefix="Ch",
    ),
    "hijii": BookConfig(
        slug="hijii",
        full_name="肘井の読解のための英文法",
        db_book_name="肘井の読解のための英文法",
        section_prefix="Hij",
    ),
}


def get_book_config(slug: str) -> BookConfig:
    """Get BookConfig by slug. Raises BookNotFoundError if not found."""
    config = BOOKS.get(slug)
    if config is None:
        raise BookNotFoundError(slug)
    return config
