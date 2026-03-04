"""Integration tests requiring real Supabase connection.

These tests are skipped unless SUPABASE_URL and SUPABASE_KEY are set.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"

requires_supabase = pytest.mark.skipif(
    not (os.environ.get("SUPABASE_URL") and os.environ.get("SUPABASE_KEY")),
    reason="SUPABASE_URL and SUPABASE_KEY must be set",
)


@requires_supabase
class TestRealDBRoundTrip:
    """Test load → delete → insert → verify with real DB."""

    def test_validate_only_with_real_fixtures(self):
        from book_importer import BookImporter

        result = BookImporter().run(str(FIXTURES), validate_only=True)
        assert result.success is True
        assert result.loaded["knowledge_nodes"] == 2

    def test_dry_run_with_real_connection(self):
        """dry_run should connect to DB but not mutate."""
        from book_importer import BookImporter

        result = BookImporter().run(str(FIXTURES), dry_run=True)
        assert result.success is True

    def test_validate_only_with_kakushin_data(self):
        """Validate kakushin_data if it exists."""
        kakushin = Path(__file__).parent.parent / "kakushin_data"
        if not kakushin.exists():
            pytest.skip("kakushin_data/ not found")

        from book_importer import BookImporter

        result = BookImporter().run(str(kakushin), validate_only=True)
        assert result.success is True, [str(e) for e in result.errors]
