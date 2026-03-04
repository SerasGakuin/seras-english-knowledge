"""FK-ordered batch insertion."""

from __future__ import annotations

from .schema import BOOKDATA_ATTR, INSERTION_ORDER
from .types import BookData

BATCH_SIZE = 100


class BookInserter:
    """Insert a BookData into the database in FK-safe order."""

    def __init__(self, client) -> None:
        self._client = client

    def insert(
        self, data: BookData, *, dry_run: bool = False
    ) -> dict[str, int]:
        """Insert all tables in INSERTION_ORDER. Returns row counts."""
        result: dict[str, int] = {table: 0 for table in INSERTION_ORDER}

        for table in INSERTION_ORDER:
            attr = BOOKDATA_ATTR[table]
            rows = getattr(data, attr)
            if not rows:
                continue
            result[table] = len(rows)
            if dry_run:
                continue
            self._batch_insert(table, rows)

        return result

    def _batch_insert(self, table: str, rows: list[dict]) -> None:
        for i in range(0, len(rows), BATCH_SIZE):
            batch = rows[i : i + BATCH_SIZE]
            self._client.table(table).insert(batch).execute()
