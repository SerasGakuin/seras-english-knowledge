"""Integration tests for SupabaseDataStore (requires live Supabase connection)."""

import os

import pytest

from app.models import CheckPoint, KnowledgeNode, SectionMapping, Sentence

# Skip entire module if Supabase credentials are not set
pytestmark = pytest.mark.skipif(
    not os.environ.get("SUPABASE_URL") or not os.environ.get("SUPABASE_KEY"),
    reason="SUPABASE_URL and SUPABASE_KEY environment variables required",
)


@pytest.fixture(scope="module")
def store():  # type: ignore[no-untyped-def]
    """Create a SupabaseDataStore connected to real Supabase."""
    from postgrest import SyncPostgrestClient

    from app.services.supabase_data_store import SupabaseDataStore

    url = os.environ["SUPABASE_URL"]
    key = os.environ["SUPABASE_KEY"]
    client = SyncPostgrestClient(
        base_url=f"{url}/rest/v1",
        headers={"apikey": key, "Authorization": f"Bearer {key}"},
    )
    return SupabaseDataStore(client)


class TestGetNode:
    def test_existing_node(self, store) -> None:  # type: ignore[no-untyped-def]
        node = store.get_node("strc-001")
        assert node is not None
        assert isinstance(node, KnowledgeNode)
        assert node.id == "strc-001"
        assert node.name != ""
        assert node.category != ""

    def test_node_has_goals(self, store) -> None:  # type: ignore[no-untyped-def]
        node = store.get_node("strc-001")
        assert node is not None
        assert len(node.understanding_goals) > 0

    def test_node_has_check_points(self, store) -> None:  # type: ignore[no-untyped-def]
        node = store.get_node("strc-001")
        assert node is not None
        assert len(node.check_points) > 0
        assert all(isinstance(cp, CheckPoint) for cp in node.check_points)

    def test_node_has_references(self, store) -> None:  # type: ignore[no-untyped-def]
        node = store.get_node("strc-001")
        assert node is not None
        assert isinstance(node.references, dict)

    def test_nonexistent_node(self, store) -> None:  # type: ignore[no-untyped-def]
        node = store.get_node("nonexistent-999")
        assert node is None

    def test_node_prerequisites(self, store) -> None:  # type: ignore[no-untyped-def]
        node = store.get_node("vtyp-001")
        assert node is not None
        assert isinstance(node.prerequisites, tuple)
        assert len(node.prerequisites) > 0


class TestGetSection:
    def test_existing_section(self, store) -> None:  # type: ignore[no-untyped-def]
        section = store.get_section("Ch01_00")
        assert section is not None
        assert isinstance(section, SectionMapping)
        assert section.id == "Ch01_00"
        assert section.title != ""

    def test_section_has_knowledge_nodes(self, store) -> None:  # type: ignore[no-untyped-def]
        section = store.get_section("Ch01_00")
        assert section is not None
        assert len(section.knowledge_nodes) > 0

    def test_section_sentence_file_is_none(self, store) -> None:  # type: ignore[no-untyped-def]
        section = store.get_section("Ch01_00")
        assert section is not None
        assert section.sentence_file is None

    def test_nonexistent_section(self, store) -> None:  # type: ignore[no-untyped-def]
        section = store.get_section("nonexistent")
        assert section is None

    def test_section_has_book_field(self, store) -> None:  # type: ignore[no-untyped-def]
        section = store.get_section("Ch01_00")
        assert section is not None
        assert section.book == "はじめの英文読解ドリル"

    def test_hijii_section_has_book_field(self, store) -> None:  # type: ignore[no-untyped-def]
        section = store.get_section("Hij_02")
        assert section is not None
        assert section.book == "肘井の読解のための英文法"


class TestGetSentences:
    def test_existing_section_sentences(self, store) -> None:  # type: ignore[no-untyped-def]
        sentences = store.get_sentences("Ch01_01")
        assert len(sentences) > 0
        assert all(isinstance(s, Sentence) for s in sentences)

    def test_sentence_fields(self, store) -> None:  # type: ignore[no-untyped-def]
        sentences = store.get_sentences("Ch01_01")
        assert len(sentences) > 0
        s = sentences[0]
        assert s.english != ""
        assert s.japanese != ""
        assert isinstance(s.structure, dict)
        assert isinstance(s.knowledge_tags, tuple)

    def test_empty_section_sentences(self, store) -> None:  # type: ignore[no-untyped-def]
        sentences = store.get_sentences("nonexistent")
        assert sentences == []


class TestGetAllSectionIds:
    def test_returns_sorted_list(self, store) -> None:  # type: ignore[no-untyped-def]
        ids = store.get_all_section_ids()
        assert len(ids) > 0
        assert ids == sorted(ids)

    def test_contains_known_section(self, store) -> None:  # type: ignore[no-untyped-def]
        ids = store.get_all_section_ids()
        assert "Ch01_00" in ids

    def test_filter_by_hajime(self, store) -> None:  # type: ignore[no-untyped-def]
        ids = store.get_all_section_ids(book="はじめの英文読解ドリル")
        assert len(ids) > 0
        assert all(sid.startswith("Ch") for sid in ids)

    def test_filter_by_hijii(self, store) -> None:  # type: ignore[no-untyped-def]
        ids = store.get_all_section_ids(book="肘井の読解のための英文法")
        assert len(ids) > 0
        assert all(sid.startswith("Hij") for sid in ids)

    def test_no_filter_returns_all(self, store) -> None:  # type: ignore[no-untyped-def]
        all_ids = store.get_all_section_ids()
        hajime_ids = store.get_all_section_ids(book="はじめの英文読解ドリル")
        hijii_ids = store.get_all_section_ids(book="肘井の読解のための英文法")
        assert len(all_ids) == len(hajime_ids) + len(hijii_ids)


class TestSectionExists:
    def test_existing_section(self, store) -> None:  # type: ignore[no-untyped-def]
        assert store.section_exists("Ch01_00") is True

    def test_nonexistent_section(self, store) -> None:  # type: ignore[no-untyped-def]
        assert store.section_exists("nonexistent") is False
