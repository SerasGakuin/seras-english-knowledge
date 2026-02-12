"""Tests for section_parser."""

import pytest

from app.models import InvalidSectionRangeError, SectionNotFoundError
from app.services.section_parser import parse_sections
from app.services.data_loader import DataStore


class TestParseNormal:
    def test_single_range(self, data_store: DataStore) -> None:
        result = parse_sections("1-0~1-1", data_store)
        assert result == ["Ch01_00", "Ch01_01"]

    def test_includes_introduction(self, data_store: DataStore) -> None:
        result = parse_sections("1-0~1-1", data_store)
        assert "Ch01_00" in result

    def test_single_section(self, data_store: DataStore) -> None:
        result = parse_sections("1-1~1-1", data_store)
        assert result == ["Ch01_01"]

    def test_comma_separated_ranges(self, data_store: DataStore) -> None:
        result = parse_sections("1-0~1-0,1-1~1-1", data_store)
        assert result == ["Ch01_00", "Ch01_01"]

    def test_comma_separated_preserves_order(self, data_store: DataStore) -> None:
        result = parse_sections("1-0~1-0,1-1~1-1", data_store)
        assert result == sorted(result)


class TestParseErrors:
    def test_nonexistent_section(self, data_store: DataStore) -> None:
        with pytest.raises(SectionNotFoundError):
            parse_sections("1-1~1-9", data_store)

    def test_reversed_range(self, data_store: DataStore) -> None:
        with pytest.raises(InvalidSectionRangeError):
            parse_sections("1-5~1-1", data_store)

    def test_malformed_input(self, data_store: DataStore) -> None:
        with pytest.raises(InvalidSectionRangeError):
            parse_sections("abc", data_store)

    def test_empty_string(self, data_store: DataStore) -> None:
        with pytest.raises(InvalidSectionRangeError):
            parse_sections("", data_store)

    def test_cross_chapter_in_single_range(self, data_store: DataStore) -> None:
        with pytest.raises(InvalidSectionRangeError):
            parse_sections("1-5~2-1", data_store)
