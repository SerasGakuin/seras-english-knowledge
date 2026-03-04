"""Book importer: YAML → Supabase pipeline."""

from __future__ import annotations

from . import client as _client
from .deleter import BookDeleter
from .inserter import BookInserter
from .loader import YamlBookLoader
from .schema import BOOKDATA_ATTR, INSERTION_ORDER
from .types import BookData, ImportResult
from .validator import ImportValidator


class BookImporter:
    """Orchestrate load → validate → delete → insert pipeline."""

    def run(
        self,
        data_dir: str,
        *,
        dry_run: bool = False,
        validate_only: bool = False,
    ) -> ImportResult:
        # 1. Load
        data = YamlBookLoader(data_dir).load()
        loaded = {
            table: len(getattr(data, BOOKDATA_ATTR[table]))
            for table in INSERTION_ORDER
        }

        # 2. Validate
        errors = ImportValidator().validate(data)
        if errors:
            return ImportResult(
                success=False,
                book_name=data.book_name,
                errors=errors,
                loaded=loaded,
            )

        if validate_only:
            return ImportResult(
                success=True,
                book_name=data.book_name,
                loaded=loaded,
            )

        # 3. Connect
        client = _client.get_supabase_client()

        # 4. Delete existing data for this book
        deleted = BookDeleter(client).delete(
            data.book_name, dry_run=dry_run
        )

        # 5. Insert
        inserted = BookInserter(client).insert(data, dry_run=dry_run)

        return ImportResult(
            success=True,
            book_name=data.book_name,
            loaded=loaded,
            deleted=deleted,
            inserted=inserted,
        )
