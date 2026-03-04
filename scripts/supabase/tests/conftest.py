"""Shared fixtures for book_importer tests."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import pytest

from book_importer.loader import YamlBookLoader
from book_importer.types import BookData

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@dataclass
class _ExecuteResult:
    data: list[dict] = field(default_factory=list)
    count: int | None = None


class _QueryBuilder:
    """Simulates PostgREST builder chain for SELECT queries."""

    def __init__(self, mock: MockSupabaseClient, table: str) -> None:
        self._mock = mock
        self._table = table
        self._select_cols: str | None = None
        self._filters: list[tuple[str, str, object]] = []
        self._op: str | None = None  # "select", "insert", "delete"
        self._insert_data: list[dict] | None = None
        self._range_start: int | None = None
        self._range_end: int | None = None

    def select(self, cols: str = "*") -> _QueryBuilder:
        self._op = "select"
        self._select_cols = cols
        return self

    def insert(self, data: list[dict]) -> _QueryBuilder:
        self._op = "insert"
        self._insert_data = data
        return self

    def delete(self) -> _QueryBuilder:
        self._op = "delete"
        return self

    def eq(self, col: str, val: object) -> _QueryBuilder:
        self._filters.append(("eq", col, val))
        return self

    def in_(self, col: str, values: list) -> _QueryBuilder:
        self._filters.append(("in_", col, values))
        return self

    def range(self, start: int, end: int) -> _QueryBuilder:
        self._range_start = start
        self._range_end = end
        return self

    def execute(self) -> _ExecuteResult:
        if self._op == "insert":
            self._mock.inserted.setdefault(self._table, []).extend(self._insert_data)
            self._mock.insert_calls.append((self._table, self._insert_data))
            return _ExecuteResult(data=self._insert_data)
        elif self._op == "delete":
            self._mock.delete_calls.append((self._table, list(self._filters)))
            # Count how many rows would be deleted
            rows = self._mock._query_results.get(self._table, [])
            count = self._count_matching(rows)
            return _ExecuteResult(data=[], count=count)
        elif self._op == "select":
            rows = self._mock._query_results.get(self._table, [])
            filtered = self._apply_filters(rows)
            if self._range_start is not None:
                filtered = filtered[self._range_start:self._range_end + 1]
            self._mock.select_calls.append((self._table, self._select_cols, list(self._filters)))
            return _ExecuteResult(data=filtered)
        return _ExecuteResult()

    def _apply_filters(self, rows: list[dict]) -> list[dict]:
        result = rows
        for op, col, val in self._filters:
            if op == "eq":
                result = [r for r in result if r.get(col) == val]
            elif op == "in_":
                result = [r for r in result if r.get(col) in val]
        return result

    def _count_matching(self, rows: list[dict]) -> int:
        return len(self._apply_filters(rows))


class MockSupabaseClient:
    """Mock Supabase client that records operations."""

    def __init__(self) -> None:
        self.inserted: dict[str, list[dict]] = {}
        self.insert_calls: list[tuple[str, list[dict]]] = []
        self.delete_calls: list[tuple[str, list]] = []
        self.select_calls: list[tuple[str, str | None, list]] = []
        self._query_results: dict[str, list[dict]] = {}

    def set_query_result(self, table: str, rows: list[dict]) -> None:
        """Pre-configure SELECT results for a table."""
        self._query_results[table] = rows

    def table(self, name: str) -> _QueryBuilder:
        return _QueryBuilder(self, name)


@pytest.fixture
def mock_client() -> MockSupabaseClient:
    return MockSupabaseClient()


@pytest.fixture
def sample_book_data() -> BookData:
    return YamlBookLoader(FIXTURES_DIR).load()
