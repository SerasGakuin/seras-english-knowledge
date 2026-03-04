"""Tests for schema constants."""

from book_importer.schema import (
    BOOKDATA_ATTR,
    DELETION_FILTERS,
    DELETION_ORDER,
    INSERTION_ORDER,
)


class TestInsertionAndDeletionOrder:
    def test_deletion_is_reverse_of_insertion(self):
        assert DELETION_ORDER == list(reversed(INSERTION_ORDER))

    def test_all_tables_present_in_both_orders(self):
        assert set(INSERTION_ORDER) == set(DELETION_ORDER)

    def test_no_duplicates_in_insertion_order(self):
        assert len(INSERTION_ORDER) == len(set(INSERTION_ORDER))

    def test_table_count(self):
        # 11 tables (excluding cross_book_links)
        assert len(INSERTION_ORDER) == 11


class TestDeletionFilters:
    def test_covers_all_tables(self):
        assert set(DELETION_FILTERS.keys()) == set(INSERTION_ORDER)

    def test_all_id_sources_are_valid(self):
        valid_sources = {"sections", "knowledge_nodes", "sentences"}
        for table, (_, source) in DELETION_FILTERS.items():
            assert source in valid_sources, f"{table} has invalid source {source}"

    def test_root_tables_filter_by_own_id(self):
        assert DELETION_FILTERS["knowledge_nodes"] == ("id", "knowledge_nodes")
        assert DELETION_FILTERS["sections"] == ("id", "sections")


class TestBookdataAttr:
    def test_covers_all_tables(self):
        assert set(BOOKDATA_ATTR.keys()) == set(INSERTION_ORDER)

    def test_attr_names_are_strings(self):
        for table, attr in BOOKDATA_ATTR.items():
            assert isinstance(attr, str), f"{table} has non-string attr {attr}"
