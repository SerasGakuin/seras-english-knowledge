"""Tests for DB-search-based book deletion."""

from book_importer.deleter import BookDeleter
from book_importer.schema import DELETION_ORDER


class TestDiscover:
    def test_discover_queries_sections_first(self, mock_client):
        mock_client.set_query_result("sections", [
            {"id": "S1", "book": "TestBook"}, {"id": "S2", "book": "TestBook"},
        ])
        mock_client.set_query_result("section_knowledge_nodes", [
            {"node_id": "n1", "section_id": "S1"},
            {"node_id": "n2", "section_id": "S2"},
        ])
        mock_client.set_query_result("sentences", [
            {"id": "s1", "section_id": "S1"}, {"id": "s2", "section_id": "S2"},
        ])
        deleter = BookDeleter(mock_client)
        deleter.discover("TestBook")

        assert len(mock_client.select_calls) >= 1
        first_call = mock_client.select_calls[0]
        assert first_call[0] == "sections"

    def test_discover_returns_all_id_sets(self, mock_client):
        mock_client.set_query_result("sections", [
            {"id": "S1", "book": "TestBook"},
        ])
        mock_client.set_query_result("section_knowledge_nodes", [
            {"node_id": "n1", "section_id": "S1"},
        ])
        mock_client.set_query_result("sentences", [
            {"id": "s1", "section_id": "S1"},
        ])

        deleter = BookDeleter(mock_client)
        ids = deleter.discover("TestBook")

        assert ids["sections"] == ["S1"]
        assert ids["knowledge_nodes"] == ["n1"]
        assert ids["sentences"] == ["s1"]

    def test_discover_empty_book_returns_empty(self, mock_client):
        mock_client.set_query_result("sections", [])
        deleter = BookDeleter(mock_client)
        ids = deleter.discover("NonExistent")

        assert ids["sections"] == []
        assert ids["knowledge_nodes"] == []
        assert ids["sentences"] == []

    def test_discover_deduplicates_node_ids(self, mock_client):
        mock_client.set_query_result("sections", [
            {"id": "S1", "book": "TestBook"}, {"id": "S2", "book": "TestBook"},
        ])
        mock_client.set_query_result("section_knowledge_nodes", [
            {"node_id": "n1", "section_id": "S1"},
            {"node_id": "n1", "section_id": "S2"},
            {"node_id": "n2", "section_id": "S2"},
        ])
        mock_client.set_query_result("sentences", [])

        deleter = BookDeleter(mock_client)
        ids = deleter.discover("TestBook")
        assert sorted(ids["knowledge_nodes"]) == ["n1", "n2"]


class TestDelete:
    def test_delete_follows_deletion_order(self, mock_client):
        mock_client.set_query_result("sections", [
            {"id": "S1", "book": "TestBook"},
        ])
        mock_client.set_query_result("section_knowledge_nodes", [
            {"node_id": "n1", "section_id": "S1"},
        ])
        mock_client.set_query_result("sentences", [
            {"id": "s1", "section_id": "S1"},
        ])

        deleter = BookDeleter(mock_client)
        deleter.delete("TestBook")

        deleted_tables = [call[0] for call in mock_client.delete_calls]
        ordered = [t for t in DELETION_ORDER if t in deleted_tables]
        assert ordered == deleted_tables

    def test_delete_skips_tables_with_no_ids(self, mock_client):
        mock_client.set_query_result("sections", [])
        deleter = BookDeleter(mock_client)
        result = deleter.delete("NonExistent")

        assert mock_client.delete_calls == []
        assert all(v == 0 for v in result.values())

    def test_delete_returns_counts(self, mock_client):
        mock_client.set_query_result("sections", [
            {"id": "S1", "book": "TestBook"},
        ])
        mock_client.set_query_result("section_knowledge_nodes", [
            {"node_id": "n1", "section_id": "S1"},
        ])
        mock_client.set_query_result("sentences", [
            {"id": "s1", "section_id": "S1"},
        ])

        deleter = BookDeleter(mock_client)
        result = deleter.delete("TestBook")

        assert isinstance(result, dict)
        for table in DELETION_ORDER:
            assert table in result

    def test_dry_run_does_not_delete(self, mock_client):
        mock_client.set_query_result("sections", [
            {"id": "S1", "book": "TestBook"},
        ])
        mock_client.set_query_result("section_knowledge_nodes", [
            {"node_id": "n1", "section_id": "S1"},
        ])
        mock_client.set_query_result("sentences", [
            {"id": "s1", "section_id": "S1"},
        ])

        deleter = BookDeleter(mock_client)
        result = deleter.delete("TestBook", dry_run=True)

        assert len(mock_client.select_calls) > 0
        assert mock_client.delete_calls == []


class TestBatchSplit:
    def test_large_id_list_is_batched(self, mock_client):
        """IN clause should be split into batches of 100."""
        section_ids = [{"id": f"S{i:04d}", "book": "TestBook"} for i in range(250)]
        mock_client.set_query_result("sections", section_ids)
        mock_client.set_query_result("section_knowledge_nodes", [])
        mock_client.set_query_result("sentences", [])

        deleter = BookDeleter(mock_client)
        deleter.delete("TestBook")

        section_deletes = [c for c in mock_client.delete_calls if c[0] == "sections"]
        assert len(section_deletes) == 3  # 100 + 100 + 50
