"""Section range parser: multi-book support.

hajime:   '1-1~1-5' -> ['Ch01_01', ..., 'Ch01_05']
hijii:    '1~5'     -> ['Hij_01_1', 'Hij_01_2', 'Hij_02', ..., 'Hij_05']
kakushin: '1~6'     -> ['Kaku_01', ..., 'Kaku_06']
          '7'       -> ['Kaku_07a', 'Kaku_07b']
scramble: '1~10'    -> ['Scr_001', ..., 'Scr_010']
narikawa: '1~3'     -> ['Nar_01_01', ..., 'Nar_03_10']  (Part-based)
nyumon:   '1~5'     -> ['Ny_01', ..., 'Ny_05']
          'G1~G5'   -> ['Ny_G01', ..., 'Ny_G05']
"""

import re

from app.book_registry import BookNotFoundError, get_book_config
from app.models import InvalidSectionRangeError, SectionNotFoundError
from app.services.data_loader import DataStore

_HAJIME_RANGE = re.compile(r"^(\d+)-(\d+)~(\d+)-(\d+)$")
_HIJII_RANGE = re.compile(r"^(\d+)~(\d+)$")
_HIJII_SINGLE = re.compile(r"^(\d+)$")
_KAKUSHIN_RANGE = re.compile(r"^(\d+)~(\d+)$")
_KAKUSHIN_SINGLE = re.compile(r"^(\d+)$")
_SCRAMBLE_RANGE = re.compile(r"^(\d+)~(\d+)$")
_SCRAMBLE_SINGLE = re.compile(r"^(\d+)$")
_NARIKAWA_RANGE = re.compile(r"^(\d+)~(\d+)$")
_NARIKAWA_SINGLE = re.compile(r"^(\d+)$")
_NYUMON_RANGE = re.compile(r"^(\d+)~(\d+)$")
_NYUMON_SINGLE = re.compile(r"^(\d+)$")
_NYUMON_G_RANGE = re.compile(r"^G(\d+)~G(\d+)$", re.IGNORECASE)
_NYUMON_G_SINGLE = re.compile(r"^G(\d+)$", re.IGNORECASE)


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
    elif book_slug == "kakushin":
        return _parse_kakushin(stripped, data_store)
    elif book_slug == "scramble":
        return _parse_scramble(stripped, data_store)
    elif book_slug == "narikawa":
        return _parse_narikawa(stripped, data_store)
    elif book_slug == "nyumon":
        return _parse_nyumon(stripped, data_store)
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


def _parse_kakushin(raw: str, data_store: DataStore) -> list[str]:
    """Parse kakushin-style range: '1~6' or '7' or '1~6,7'.

    Theme number T maps to all sections matching 'Kaku_{T:02d}' prefix.
    Split themes (e.g., Kaku_07a, Kaku_07b) are automatically included.
    """
    parts = [p.strip() for p in raw.split(",")]
    result: list[str] = []
    for part in parts:
        result.extend(_parse_kakushin_single(part, data_store))
    # Deduplicate while preserving order, then sort
    seen: set[str] = set()
    unique: list[str] = []
    for sid in result:
        if sid not in seen:
            seen.add(sid)
            unique.append(sid)
    return sorted(unique)


def _parse_kakushin_single(part: str, data_store: DataStore) -> list[str]:
    # Try range pattern first: "1~6"
    range_match = _KAKUSHIN_RANGE.match(part)
    if range_match:
        start = int(range_match.group(1))
        end = int(range_match.group(2))
        if start > end:
            raise InvalidSectionRangeError(
                detail=f"Reversed range: '{part}'. Start must be <= end."
            )
        return _expand_kakushin_themes(start, end, data_store)

    # Try single theme: "7"
    single_match = _KAKUSHIN_SINGLE.match(part)
    if single_match:
        theme = int(single_match.group(1))
        return _expand_kakushin_themes(theme, theme, data_store)

    raise InvalidSectionRangeError(
        detail=f"Invalid section range format: '{part}'. "
        "Expected format for kakushin: 'T1~T2' (e.g., '1~6') or single theme 'T' (e.g., '7')"
    )


def _expand_kakushin_themes(
    start: int, end: int, data_store: DataStore
) -> list[str]:
    """Expand theme range to matching section IDs from DB.

    Kaku_07a, Kaku_07b are both matched by theme 7.
    Uses 2-digit zero-padding to prevent prefix collisions (Kaku_01 vs Kaku_10).
    """
    book_name = "英文法の核心"
    all_sections = data_store.get_all_section_ids(book=book_name)

    result: list[str] = []
    for theme in range(start, end + 1):
        prefix = f"Kaku_{theme:02d}"
        matched = [
            sid for sid in all_sections
            if sid == prefix  # exact match (Kaku_01)
            or (
                sid.startswith(prefix)
                and len(sid) > len(prefix)
                and sid[len(prefix)].isalpha()  # alpha suffix only (Kaku_07a)
            )
        ]
        if not matched:
            raise SectionNotFoundError(
                detail=f"No sections found for theme {theme} (prefix '{prefix}')"
            )
        result.extend(matched)

    return result


# ---- scramble ----


def _parse_scramble(raw: str, data_store: DataStore) -> list[str]:
    """Parse scramble-style range: '1~10' or '5' or '1~10,15~20'.

    Number N maps to section 'Scr_{N:03d}'.
    """
    parts = [p.strip() for p in raw.split(",")]
    result: list[str] = []
    for part in parts:
        result.extend(_parse_scramble_single(part, data_store))
    return result


def _parse_scramble_single(part: str, data_store: DataStore) -> list[str]:
    range_match = _SCRAMBLE_RANGE.match(part)
    if range_match:
        start = int(range_match.group(1))
        end = int(range_match.group(2))
        if start > end:
            raise InvalidSectionRangeError(
                detail=f"Reversed range: '{part}'. Start must be <= end."
            )
        section_ids: list[str] = []
        for n in range(start, end + 1):
            section_id = f"Scr_{n:03d}"
            if not data_store.section_exists(section_id):
                raise SectionNotFoundError(
                    detail=f"Section {section_id} does not exist"
                )
            section_ids.append(section_id)
        return section_ids

    single_match = _SCRAMBLE_SINGLE.match(part)
    if single_match:
        n = int(single_match.group(1))
        section_id = f"Scr_{n:03d}"
        if not data_store.section_exists(section_id):
            raise SectionNotFoundError(
                detail=f"Section {section_id} does not exist"
            )
        return [section_id]

    raise InvalidSectionRangeError(
        detail=f"Invalid section range format: '{part}'. "
        "Expected format for scramble: 'N1~N2' (e.g., '1~10') or single 'N' (e.g., '5')"
    )


# ---- narikawa ----


def _parse_narikawa(raw: str, data_store: DataStore) -> list[str]:
    """Parse narikawa-style range: '1~3' or '5' or '1~3,7'.

    Part number P maps to all sections matching 'Nar_{P:02d}_' prefix.
    """
    parts = [p.strip() for p in raw.split(",")]
    result: list[str] = []
    for part in parts:
        result.extend(_parse_narikawa_single(part, data_store))
    seen: set[str] = set()
    unique: list[str] = []
    for sid in result:
        if sid not in seen:
            seen.add(sid)
            unique.append(sid)
    return sorted(unique)


def _parse_narikawa_single(part: str, data_store: DataStore) -> list[str]:
    range_match = _NARIKAWA_RANGE.match(part)
    if range_match:
        start = int(range_match.group(1))
        end = int(range_match.group(2))
        if start > end:
            raise InvalidSectionRangeError(
                detail=f"Reversed range: '{part}'. Start must be <= end."
            )
        return _expand_narikawa_parts(start, end, data_store)

    single_match = _NARIKAWA_SINGLE.match(part)
    if single_match:
        part_num = int(single_match.group(1))
        return _expand_narikawa_parts(part_num, part_num, data_store)

    raise InvalidSectionRangeError(
        detail=f"Invalid section range format: '{part}'. "
        "Expected format for narikawa: 'P1~P2' (e.g., '1~3') or single part 'P' (e.g., '5')"
    )


def _expand_narikawa_parts(
    start: int, end: int, data_store: DataStore
) -> list[str]:
    """Expand part range to matching section IDs from DB."""
    book_name = "成川の深めて解ける！英文法 INPUT"
    all_sections = data_store.get_all_section_ids(book=book_name)

    result: list[str] = []
    for part in range(start, end + 1):
        prefix = f"Nar_{part:02d}_"
        matched = [sid for sid in all_sections if sid.startswith(prefix)]
        if not matched:
            raise SectionNotFoundError(
                detail=f"No sections found for part {part} (prefix '{prefix}')"
            )
        result.extend(matched)

    return result


# ---- nyumon ----


def _parse_nyumon(raw: str, data_store: DataStore) -> list[str]:
    """Parse nyumon-style range: '1~5' or 'G1~G5' or '1~5,G1~G5'.

    Number N maps to sections matching 'Ny_{N:02d}' prefix.
    'G' prefix maps to sections matching 'Ny_G{N:02d}' prefix.
    """
    parts = [p.strip() for p in raw.split(",")]
    result: list[str] = []
    for part in parts:
        result.extend(_parse_nyumon_single(part, data_store))
    seen: set[str] = set()
    unique: list[str] = []
    for sid in result:
        if sid not in seen:
            seen.add(sid)
            unique.append(sid)
    return sorted(unique)


def _parse_nyumon_single(part: str, data_store: DataStore) -> list[str]:
    # G-prefix range: "G1~G5"
    g_range = _NYUMON_G_RANGE.match(part)
    if g_range:
        start = int(g_range.group(1))
        end = int(g_range.group(2))
        if start > end:
            raise InvalidSectionRangeError(
                detail=f"Reversed range: '{part}'. Start must be <= end."
            )
        return _expand_nyumon_sections(start, end, data_store, g_prefix=True)

    # G-prefix single: "G5"
    g_single = _NYUMON_G_SINGLE.match(part)
    if g_single:
        n = int(g_single.group(1))
        return _expand_nyumon_sections(n, n, data_store, g_prefix=True)

    # Numeric range: "1~5"
    range_match = _NYUMON_RANGE.match(part)
    if range_match:
        start = int(range_match.group(1))
        end = int(range_match.group(2))
        if start > end:
            raise InvalidSectionRangeError(
                detail=f"Reversed range: '{part}'. Start must be <= end."
            )
        return _expand_nyumon_sections(start, end, data_store, g_prefix=False)

    # Numeric single: "5"
    single_match = _NYUMON_SINGLE.match(part)
    if single_match:
        n = int(single_match.group(1))
        return _expand_nyumon_sections(n, n, data_store, g_prefix=False)

    raise InvalidSectionRangeError(
        detail=f"Invalid section range format: '{part}'. "
        "Expected format for nyumon: 'N1~N2' (e.g., '1~5'), 'G1~G5', "
        "or single 'N'/'GN' (e.g., '5', 'G3')"
    )


def _expand_nyumon_sections(
    start: int, end: int, data_store: DataStore, *, g_prefix: bool
) -> list[str]:
    """Expand nyumon section range to matching section IDs from DB."""
    book_name = "入門英文問題精講"
    all_sections = data_store.get_all_section_ids(book=book_name)

    result: list[str] = []
    for n in range(start, end + 1):
        if g_prefix:
            section_id = f"Ny_G{n:02d}"
        else:
            section_id = f"Ny_{n:02d}"
        matched = [sid for sid in all_sections if sid == section_id]
        if not matched:
            raise SectionNotFoundError(
                detail=f"Section {section_id} does not exist"
            )
        result.extend(matched)

    return result
