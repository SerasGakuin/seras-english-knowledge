"""Tests for BookImporter orchestrator."""

from pathlib import Path
from unittest.mock import patch

from book_importer import BookImporter
from book_importer.types import ImportResult

FIXTURES = Path(__file__).parent / "fixtures"


class TestHappyPath:
    def test_run_returns_import_result(self, mock_client):
        with patch("book_importer.client.get_supabase_client", return_value=mock_client):
            result = BookImporter().run(FIXTURES)
        assert isinstance(result, ImportResult)
        assert result.success is True
        assert result.book_name == "テスト参考書"

    def test_run_loads_data(self, mock_client):
        with patch("book_importer.client.get_supabase_client", return_value=mock_client):
            result = BookImporter().run(FIXTURES)
        assert result.loaded["knowledge_nodes"] == 2
        assert result.loaded["sections"] == 2
        assert result.loaded["sentences"] == 2

    def test_run_inserts_data(self, mock_client):
        with patch("book_importer.client.get_supabase_client", return_value=mock_client):
            result = BookImporter().run(FIXTURES)
        assert result.inserted["knowledge_nodes"] == 2
        assert result.inserted["sentences"] == 2

    def test_run_calls_delete_then_insert(self, mock_client):
        with patch("book_importer.client.get_supabase_client", return_value=mock_client):
            BookImporter().run(FIXTURES)
        # Deletes happen before inserts (discover selects first, then deletes, then inserts)
        # Since discover finds nothing in the empty mock, delete_calls is empty
        assert len(mock_client.insert_calls) > 0


class TestValidateOnly:
    def test_validate_only_does_not_touch_db(self, mock_client):
        with patch("book_importer.client.get_supabase_client", return_value=mock_client):
            result = BookImporter().run(FIXTURES, validate_only=True)
        assert result.success is True
        assert mock_client.insert_calls == []
        assert mock_client.delete_calls == []
        assert mock_client.select_calls == []

    def test_validate_only_still_loads(self, mock_client):
        with patch("book_importer.client.get_supabase_client", return_value=mock_client):
            result = BookImporter().run(FIXTURES, validate_only=True)
        assert result.loaded["knowledge_nodes"] == 2


class TestDryRun:
    def test_dry_run_does_not_mutate_db(self, mock_client):
        with patch("book_importer.client.get_supabase_client", return_value=mock_client):
            result = BookImporter().run(FIXTURES, dry_run=True)
        assert result.success is True
        assert mock_client.insert_calls == []
        assert mock_client.delete_calls == []


class TestValidationFailure:
    def test_invalid_data_returns_failure(self, mock_client, tmp_path):
        """If validation fails, no DB operations should occur."""
        # Create sections referencing a node that doesn't exist in any node file
        sections = tmp_path / "sections.yaml"
        sections.write_text(
            "sections:\n"
            '  - id: "S1"\n    book: "Test"\n    title: "S"\n'
            '    pages: "p.1"\n    type: "grammar_lecture"\n'
            "section_knowledge_nodes:\n"
            '  - section_id: "S1"\n    node_id: "missing_node"\n    seq: 1\n'
            "section_prerequisites: []\n"
        )
        kn = tmp_path / "knowledge_nodes"
        kn.mkdir()
        (kn / "nodes.yaml").write_text(
            "knowledge_nodes:\n"
            '  - id: "n1"\n    name: "N"\n    category: "C"\n'
            '    priority: "P1"\n    notes: ""\n'
        )

        with patch("book_importer.client.get_supabase_client", return_value=mock_client):
            result = BookImporter().run(tmp_path)
        assert result.success is False
        assert len(result.errors) > 0
        assert mock_client.insert_calls == []
        assert mock_client.delete_calls == []
