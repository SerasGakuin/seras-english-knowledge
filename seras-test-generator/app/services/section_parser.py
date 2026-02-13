"""Section range parser: multi-book support.

hajime: '1-1~1-5' -> ['Ch01_01', ..., 'Ch01_05']
hijii:  '1~5'     -> ['Hij_01_1', 'Hij_01_2', 'Hij_02', ..., 'Hij_05']
"""

import re

from app.book_registry import BookNotFoundError, get_book_config
from app.models import InvalidSectionRangeError, SectionNotFoundError
from app.services.data_loader import DataStore

_HAJIME_RANGE = re.compile(r"^(\d+)-(\d+)~(\d+)-(\d+)$")
_HIJII_RANGE = re.compile(r"^(\d+)~(\d+)$")
_HIJII_SINGLE = re.compile(r"^(\d+)$")


def parse_sections(
    raw: str, data_store: DataStore, book_slug: str = "hajime"
) -> list[str]:
    """Parse section range string into a list of section IDs.

    Args:
        raw: Range string (format depends on book)
        data_store: DataStore instance for existence validation
        book_slug: Book identifier ("hajime" or "hijii")

    Returns:
        List of section IDs

    Raises:
        InvalidSectionRangeError: Malformed input or reversed range
        SectionNotFoundError: Section ID does not exist in data
        BookNotFoundError: Unknown book slug
    """
    stripped = raw.strip()
    if not stripped:
        raise InvalidSectionRangeError(detail="Section range cannot be empty")

    # Validate book slug
    get_book_config(book_slug)

    if book_slug == "hajime":
        return _parse_hajime(stripped, data_store)
    elif book_slug == "hijii":
        return _parse_hijii(stripped, data_store)
    else:
        raise BookNotFoundError(book_slug)


def _parse_hajime(raw: str, data_store: DataStore) -> list[str]:
    """Parse hajime-style range: '1-0~1-1' or '1-0~1-0,1-1~1-1'."""
    parts = [p.strip() for p in raw.split(",")]
    result: list[str] = []
    for part in parts:
        result.extend(_parse_hajime_single(part, data_store))
    return result


def _parse_hajime_single(part: str, data_store: DataStore) -> list[str]:
    match = _HAJIME_RANGE.match(part)
    if not match:
        raise InvalidSectionRangeError(
            detail=f"Invalid section range format: '{part}'. "
            "Expected format: 'X-Y~X-Z' (e.g., '1-1~1-5')"
        )

    ch_start, sec_start, ch_end, sec_end = (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
        int(match.group(4)),
    )

    if ch_start != ch_end:
        raise InvalidSectionRangeError(
            detail=f"Cross-chapter range not allowed: '{part}'. "
            "Use comma-separated ranges for multiple chapters."
        )

    if sec_start > sec_end:
        raise InvalidSectionRangeError(
            detail=f"Reversed range: '{part}'. Start must be <= end."
        )

    chapter = ch_start
    section_ids: list[str] = []
    for sec in range(sec_start, sec_end + 1):
        section_id = f"Ch{chapter:02d}_{sec:02d}"
        if not data_store.section_exists(section_id):
            raise SectionNotFoundError(
                detail=f"Section {section_id} does not exist"
            )
        section_ids.append(section_id)

    return section_ids


def _parse_hijii(raw: str, data_store: DataStore) -> list[str]:
    """Parse hijii-style range: '1~5' or '7' or '1~5,8~10'.

    Theme number T maps to all sections matching 'Hij_{T:02d}' prefix.
    Split themes (e.g., Hij_01_1, Hij_01_2) are automatically included.
    """
    parts = [p.strip() for p in raw.split(",")]
    result: list[str] = []
    for part in parts:
        result.extend(_parse_hijii_single(part, data_store))
    # Deduplicate while preserving order, then sort
    seen: set[str] = set()
    unique: list[str] = []
    for sid in result:
        if sid not in seen:
            seen.add(sid)
            unique.append(sid)
    return sorted(unique)


def _parse_hijii_single(part: str, data_store: DataStore) -> list[str]:
    # Try range pattern first: "1~5"
    range_match = _HIJII_RANGE.match(part)
    if range_match:
        start = int(range_match.group(1))
        end = int(range_match.group(2))
        if start > end:
            raise InvalidSectionRangeError(
                detail=f"Reversed range: '{part}'. Start must be <= end."
            )
        return _expand_hijii_themes(start, end, data_store)

    # Try single theme: "7"
    single_match = _HIJII_SINGLE.match(part)
    if single_match:
        theme = int(single_match.group(1))
        return _expand_hijii_themes(theme, theme, data_store)

    raise InvalidSectionRangeError(
        detail=f"Invalid section range format: '{part}'. "
        "Expected format for hijii: 'T1~T2' (e.g., '1~5') or single theme 'T' (e.g., '7')"
    )


def _expand_hijii_themes(
    start: int, end: int, data_store: DataStore
) -> list[str]:
    """Expand theme range to matching section IDs from DB."""
    book_name = "肘井の読解のための英文法"
    all_sections = data_store.get_all_section_ids(book=book_name)

    result: list[str] = []
    for theme in range(start, end + 1):
        prefix = f"Hij_{theme:02d}"
        matched = [sid for sid in all_sections if sid == prefix or sid.startswith(prefix + "_")]
        if not matched:
            raise SectionNotFoundError(
                detail=f"No sections found for theme {theme} (prefix '{prefix}')"
            )
        result.extend(matched)

    return result
