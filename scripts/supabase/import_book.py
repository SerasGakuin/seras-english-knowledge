#!/usr/bin/env python3
"""CLI entry point for the generic book importer.

Usage:
    python scripts/supabase/import_book.py kakushin_data/
    python scripts/supabase/import_book.py scramble_data/ --dry-run
    python scripts/supabase/import_book.py narikawa_data/ --validate-only
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from book_importer import BookImporter
from book_importer.schema import INSERTION_ORDER


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Import a book's YAML data into Supabase."
    )
    parser.add_argument(
        "data_dir",
        help="Path to the book's data directory (e.g. kakushin_data/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and show what would be done, but don't modify DB.",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Only run validation (no DB connection needed).",
    )
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    if not data_dir.is_absolute():
        # Resolve relative to scripts/supabase/
        data_dir = Path(__file__).parent / data_dir

    if not data_dir.is_dir():
        print(f"Error: {data_dir} is not a directory")
        sys.exit(1)

    print(f"=== Book Importer ===")
    print(f"Data dir: {data_dir}")
    mode = "validate-only" if args.validate_only else ("dry-run" if args.dry_run else "LIVE")
    print(f"Mode: {mode}")
    print()

    result = BookImporter().run(
        str(data_dir),
        dry_run=args.dry_run,
        validate_only=args.validate_only,
    )

    # Print loaded counts
    print(f"Book: {result.book_name}")
    print(f"\n--- Loaded from YAML ---")
    for table in INSERTION_ORDER:
        count = result.loaded.get(table, 0)
        if count:
            print(f"  {table}: {count}")

    if not result.success:
        print(f"\n--- Validation FAILED ({len(result.errors)} errors) ---")
        for err in result.errors:
            print(f"  {err}")
        sys.exit(1)

    if args.validate_only:
        print(f"\nValidation passed.")
        return

    # Print deleted counts
    if result.deleted:
        print(f"\n--- Deleted from DB ---")
        for table in INSERTION_ORDER:
            count = result.deleted.get(table, 0)
            if count:
                print(f"  {table}: {count}")

    # Print inserted counts
    if result.inserted:
        print(f"\n--- Inserted into DB ---")
        for table in INSERTION_ORDER:
            count = result.inserted.get(table, 0)
            if count:
                print(f"  {table}: {count}")

    if args.dry_run:
        print(f"\nDry run complete. No changes were made.")
    else:
        print(f"\nImport complete.")


if __name__ == "__main__":
    main()
