"""DB-search-based selective deletion for a single book."""

from __future__ import annotations

from .schema import DELETION_FILTERS, DELETION_ORDER

BATCH_SIZE = 100
PAGE_SIZE = 1000


class BookDeleter:
    """Delete all data belonging to a single book from the database."""

    def __init__(self, client) -> None:
        self._client = client

    def discover(self, book_name: str) -> dict[str, list[str]]:
        """Query DB to find all IDs belonging to the given book."""
        # 1. Find sections by book name
        section_ids = self._select_all_with_eq("sections", "id", "book", book_name)

        if not section_ids:
            return {"sections": [], "knowledge_nodes": [], "sentences": []}

        # 2. Find node IDs via section_knowledge_nodes
        node_ids = self._select_all_with_in(
            "section_knowledge_nodes", "node_id", "section_id", section_ids
        )
        # Deduplicate
        node_ids = list(dict.fromkeys(node_ids))

        # 3. Find sentence IDs via sentences
        sentence_ids = self._select_all_with_in(
            "sentences", "id", "section_id", section_ids
        )

        return {
            "sections": section_ids,
            "knowledge_nodes": node_ids,
            "sentences": sentence_ids,
        }

    def delete(
        self, book_name: str, *, dry_run: bool = False
    ) -> dict[str, int]:
        """Delete all data for the given book in FK-safe order."""
        ids = self.discover(book_name)
        result: dict[str, int] = {table: 0 for table in DELETION_ORDER}

        if not any(ids.values()):
            return result

        if dry_run:
            return result

        for table in DELETION_ORDER:
            filter_col, id_source = DELETION_FILTERS[table]
            id_list = ids.get(id_source, [])
            if not id_list:
                continue
            count = self._batch_delete(table, filter_col, id_list)
            result[table] = count

        return result

    def _select_all_with_eq(
        self, table: str, select_col: str, filter_col: str, filter_val: str
    ) -> list[str]:
        """SELECT select_col FROM table WHERE filter_col = filter_val, with pagination."""
        all_ids: list[str] = []
        offset = 0
        while True:
            resp = (
                self._client.table(table)
                .select(select_col)
                .eq(filter_col, filter_val)
                .range(offset, offset + PAGE_SIZE - 1)
                .execute()
            )
            rows = resp.data
            all_ids.extend(r[select_col] for r in rows)
            if len(rows) < PAGE_SIZE:
                break
            offset += PAGE_SIZE
        return all_ids

    def _select_all_with_in(
        self, table: str, select_col: str, filter_col: str, filter_values: list[str]
    ) -> list[str]:
        """SELECT select_col FROM table WHERE filter_col IN (...), batched."""
        all_ids: list[str] = []
        for i in range(0, len(filter_values), BATCH_SIZE):
            batch = filter_values[i : i + BATCH_SIZE]
            offset = 0
            while True:
                resp = (
                    self._client.table(table)
                    .select(select_col)
                    .in_(filter_col, batch)
                    .range(offset, offset + PAGE_SIZE - 1)
                    .execute()
                )
                rows = resp.data
                all_ids.extend(r[select_col] for r in rows)
                if len(rows) < PAGE_SIZE:
                    break
                offset += PAGE_SIZE
        return all_ids

    def _batch_delete(
        self, table: str, filter_col: str, id_list: list[str]
    ) -> int:
        """Delete rows where filter_col IN id_list, batched by BATCH_SIZE."""
        total = 0
        for i in range(0, len(id_list), BATCH_SIZE):
            batch = id_list[i : i + BATCH_SIZE]
            self._client.table(table).delete().in_(filter_col, batch).execute()
            total += len(batch)
        return total
