"""Section range parser: '1-1~1-5' -> ['Ch01_01', ..., 'Ch01_05']."""

import re

from app.models import InvalidSectionRangeError, SectionNotFoundError
from app.services.data_loader import DataStore

_RANGE_PATTERN = re.compile(r"^(\d+)-(\d+)~(\d+)-(\d+)$")


def parse_sections(raw: str, data_store: DataStore) -> list[str]:
    """Parse section range string into a list of section IDs.

    Args:
        raw: Range string like "1-1~1-5" or "1-1~1-3,2-1~2-4"
        data_store: DataStore instance for existence validation

    Returns:
        Sorted list of section IDs like ["Ch01_01", ..., "Ch01_05"]

    Raises:
        InvalidSectionRangeError: Malformed input, reversed range, or cross-chapter
        SectionNotFoundError: Section ID does not exist in data
    """
    stripped = raw.strip()
    if not stripped:
        raise InvalidSectionRangeError(detail="Section range cannot be empty")

    parts = [p.strip() for p in stripped.split(",")]
    result: list[str] = []

    for part in parts:
        result.extend(_parse_single_range(part, data_store))

    return result


def _parse_single_range(part: str, data_store: DataStore) -> list[str]:
    match = _RANGE_PATTERN.match(part)
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
