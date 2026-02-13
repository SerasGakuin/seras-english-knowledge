"""Tests for book_registry."""

import pytest

from app.book_registry import BookNotFoundError, get_book_config


class TestGetBookConfig:
    def test_hajime(self) -> None:
        config = get_book_config("hajime")
        assert config.slug == "hajime"
        assert config.full_name == "はじめの英文読解ドリル"
        assert config.db_book_name == "はじめの英文読解ドリル"
        assert config.section_prefix == "Ch"

    def test_hijii(self) -> None:
        config = get_book_config("hijii")
        assert config.slug == "hijii"
        assert config.full_name == "肘井の読解のための英文法"
        assert config.db_book_name == "肘井の読解のための英文法"
        assert config.section_prefix == "Hij"

    def test_unknown_raises(self) -> None:
        with pytest.raises(BookNotFoundError):
            get_book_config("unknown")

    def test_error_message_contains_available(self) -> None:
        with pytest.raises(BookNotFoundError) as exc_info:
            get_book_config("foo")
        assert "hajime" in str(exc_info.value.detail)
        assert "hijii" in str(exc_info.value.detail)
