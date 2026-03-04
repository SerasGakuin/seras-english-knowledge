"""Tests for FK-ordered batch insertion."""

from book_importer.inserter import BookInserter
from book_importer.schema import BOOKDATA_ATTR, INSERTION_ORDER


class TestInsertionOrder:
    def test_inserts_follow_insertion_order(self, mock_client, sample_book_data):
        inserter = BookInserter(mock_client)
        inserter.insert(sample_book_data)

        inserted_tables = [call[0] for call in mock_client.insert_calls]
        # Only tables with data should appear, but in correct order
        ordered = [t for t in INSERTION_ORDER if t in inserted_tables]
        assert ordered == inserted_tables

    def test_all_nonempty_tables_inserted(self, mock_client, sample_book_data):
        inserter = BookInserter(mock_client)
        result = inserter.insert(sample_book_data)

        for table in INSERTION_ORDER:
            attr = BOOKDATA_ATTR[table]
            data = getattr(sample_book_data, attr)
            if data:
                assert result[table] == len(data), f"{table} count mismatch"
            else:
                assert result[table] == 0


class TestBatchInsertion:
    def test_large_dataset_is_batched(self, mock_client, sample_book_data):
        """Tables with >100 rows should be split into batches."""
        # Add 250 extra sentences
        for i in range(250):
            sample_book_data.sentences.append({
                "id": f"extra-{i:04d}",
                "section_id": "Test_01",
                "drill": 0,
                "number": i + 100,
                "role": "example",
                "english": f"Extra {i}",
                "japanese": f"追加 {i}",
                "notes": "",
            })

        inserter = BookInserter(mock_client)
        inserter.insert(sample_book_data)

        sentence_inserts = [c for c in mock_client.insert_calls if c[0] == "sentences"]
        # 252 sentences (2 original + 250 extra) → 3 batches
        assert len(sentence_inserts) == 3

    def test_empty_table_not_inserted(self, mock_client, sample_book_data):
        """Tables with no data should not generate insert calls."""
        # Ensure section_prerequisites is empty in fixture won't cause issues
        inserter = BookInserter(mock_client)
        inserter.insert(sample_book_data)

        inserted_tables = [call[0] for call in mock_client.insert_calls]
        for table in INSERTION_ORDER:
            attr = BOOKDATA_ATTR[table]
            data = getattr(sample_book_data, attr)
            if not data:
                assert table not in inserted_tables, f"{table} should not be inserted (empty)"


class TestDryRun:
    def test_dry_run_does_not_insert(self, mock_client, sample_book_data):
        inserter = BookInserter(mock_client)
        result = inserter.insert(sample_book_data, dry_run=True)

        assert mock_client.insert_calls == []
        # Counts should still reflect what would be inserted
        assert result["knowledge_nodes"] == 2
        assert result["sentences"] == 2


class TestReturnCounts:
    def test_returns_all_table_counts(self, mock_client, sample_book_data):
        inserter = BookInserter(mock_client)
        result = inserter.insert(sample_book_data)

        for table in INSERTION_ORDER:
            assert table in result
