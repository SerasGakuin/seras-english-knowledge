"""Tests for DataStore."""

from app.models import CheckPoint
from app.services.data_loader import DataStore


class TestLoadKnowledgeNodes:
    def test_loads_knowledge_node(self, data_store: DataStore) -> None:
        node = data_store.get_node("strc-001")
        assert node is not None

    def test_node_has_correct_fields(self, data_store: DataStore) -> None:
        node = data_store.get_node("strc-001")
        assert node is not None
        assert node.name == "主要素（S・V・O・C）の定義"
        assert node.priority == "P1"
        assert isinstance(node.check_points, tuple)
        assert len(node.check_points) == 3
        assert isinstance(node.check_points[0], CheckPoint)
        assert node.check_points[1].question == "Cになれる品詞は？"
        assert node.check_points[1].answer == "形容詞と名詞"

    def test_nonexistent_node_returns_none(self, data_store: DataStore) -> None:
        assert data_store.get_node("zzz-999") is None


class TestLoadSectionMappings:
    def test_loads_section_mapping(self, data_store: DataStore) -> None:
        section = data_store.get_section("Ch01_01")
        assert section is not None

    def test_section_has_knowledge_nodes(self, data_store: DataStore) -> None:
        section = data_store.get_section("Ch01_01")
        assert section is not None
        assert "strc-007" in section.knowledge_nodes

    def test_section_exists_true(self, data_store: DataStore) -> None:
        assert data_store.section_exists("Ch01_01")

    def test_section_exists_false(self, data_store: DataStore) -> None:
        assert not data_store.section_exists("Ch99_99")

    def test_all_section_ids_ordered(self, data_store: DataStore) -> None:
        ids = data_store.get_all_section_ids()
        assert ids == sorted(ids)
        assert "Ch01_00" in ids
        assert "Ch01_01" in ids


class TestLoadSentences:
    def test_loads_sentences(self, data_store: DataStore) -> None:
        sentences = data_store.get_sentences("Ch01_01")
        assert len(sentences) > 0

    def test_sentence_count(self, data_store: DataStore) -> None:
        sentences = data_store.get_sentences("Ch01_01")
        assert len(sentences) == 5

    def test_introduction_has_no_sentences(self, data_store: DataStore) -> None:
        sentences = data_store.get_sentences("Ch01_00")
        assert sentences == []
