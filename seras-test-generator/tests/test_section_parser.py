"""Tests for section_parser."""

import pytest

from app.book_registry import BookNotFoundError
from app.models import InvalidSectionRangeError, SectionNotFoundError
from app.services.section_parser import parse_sections
from app.services.data_loader import DataStore


class TestParseHajimeNormal:
    def test_single_range(self, data_store: DataStore) -> None:
        result = parse_sections("1-0~1-1", data_store)
        assert result == ["Ch01_00", "Ch01_01"]

    def test_explicit_book_slug(self, data_store: DataStore) -> None:
        result = parse_sections("1-0~1-1", data_store, book_slug="hajime")
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


class TestParseHajimeErrors:
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


class TestParseHijiiNormal:
    def test_single_theme_range(self, data_store: DataStore) -> None:
        result = parse_sections("2~3", data_store, book_slug="hijii")
        assert "Hij_02" in result
        assert "Hij_03" in result

    def test_single_theme(self, data_store: DataStore) -> None:
        result = parse_sections("2", data_store, book_slug="hijii")
        assert result == ["Hij_02"]

    def test_comma_separated(self, data_store: DataStore) -> None:
        result = parse_sections("2,3", data_store, book_slug="hijii")
        assert result == ["Hij_02", "Hij_03"]

    def test_sorted_output(self, data_store: DataStore) -> None:
        result = parse_sections("2~3", data_store, book_slug="hijii")
        assert result == sorted(result)


class TestParseHijiiErrors:
    def test_reversed_range(self, data_store: DataStore) -> None:
        with pytest.raises(InvalidSectionRangeError):
            parse_sections("5~1", data_store, book_slug="hijii")

    def test_nonexistent_theme(self, data_store: DataStore) -> None:
        with pytest.raises(SectionNotFoundError):
            parse_sections("99", data_store, book_slug="hijii")

    def test_invalid_format(self, data_store: DataStore) -> None:
        with pytest.raises(InvalidSectionRangeError):
            parse_sections("abc", data_store, book_slug="hijii")


class TestParseBookErrors:
    def test_unknown_book(self, data_store: DataStore) -> None:
        with pytest.raises(BookNotFoundError):
            parse_sections("1~5", data_store, book_slug="unknown")
