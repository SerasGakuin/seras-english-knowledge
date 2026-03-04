"""Tests for YAML book loader."""

from pathlib import Path

import pytest

from book_importer.loader import YamlBookLoader
from book_importer.types import BookData

FIXTURES = Path(__file__).parent / "fixtures"


class TestYamlBookLoader:
    def test_load_returns_book_data(self):
        data = YamlBookLoader(FIXTURES).load()
        assert isinstance(data, BookData)

    def test_book_name_from_sections(self):
        data = YamlBookLoader(FIXTURES).load()
        assert data.book_name == "テスト参考書"

    def test_sections_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.sections) == 2
        assert data.sections[0]["id"] == "Test_01"
        assert data.sections[1]["id"] == "Test_02"

    def test_section_knowledge_nodes_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.section_knowledge_nodes) == 3

    def test_section_prerequisites_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.section_prerequisites) == 1
        assert data.section_prerequisites[0]["section_id"] == "Test_02"

    def test_knowledge_nodes_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.knowledge_nodes) == 2
        assert data.knowledge_nodes[0]["id"] == "tst-001"

    def test_understanding_goals_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.understanding_goals) == 2

    def test_check_points_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.check_points) == 1

    def test_node_prerequisites_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.node_prerequisites) == 1

    def test_knowledge_references_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.knowledge_references) == 1

    def test_sentences_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.sentences) == 2
        assert data.sentences[0]["id"] == "tst-01-e01"

    def test_sentence_structures_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.sentence_structures) == 2

    def test_sentence_knowledge_tags_loaded(self):
        data = YamlBookLoader(FIXTURES).load()
        assert len(data.sentence_knowledge_tags) == 2

    def test_missing_sections_file_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError, match="sections.yaml"):
            YamlBookLoader(tmp_path).load()

    def test_empty_knowledge_nodes_dir(self, tmp_path):
        """If knowledge_nodes/ dir doesn't exist, lists are empty."""
        sections = tmp_path / "sections.yaml"
        sections.write_text(
            'sections:\n  - id: "S1"\n    book: "Test"\n    title: "S"\n'
            '    pages: "p.1"\n    type: "grammar_lecture"\n'
            "section_knowledge_nodes: []\nsection_prerequisites: []\n"
        )
        data = YamlBookLoader(tmp_path).load()
        assert data.knowledge_nodes == []
        assert data.sentences == []

    def test_multiple_node_files_merged(self, tmp_path):
        """Multiple YAML files in knowledge_nodes/ are merged."""
        sections = tmp_path / "sections.yaml"
        sections.write_text(
            'sections:\n  - id: "S1"\n    book: "Test"\n    title: "S"\n'
            '    pages: "p.1"\n    type: "grammar_lecture"\n'
            "section_knowledge_nodes: []\nsection_prerequisites: []\n"
        )
        kn_dir = tmp_path / "knowledge_nodes"
        kn_dir.mkdir()
        (kn_dir / "a.yaml").write_text(
            'knowledge_nodes:\n  - id: "n1"\n    name: "N1"\n'
            '    category: "C"\n    priority: "P1"\n    notes: ""\n'
        )
        (kn_dir / "b.yaml").write_text(
            'knowledge_nodes:\n  - id: "n2"\n    name: "N2"\n'
            '    category: "C"\n    priority: "P1"\n    notes: ""\n'
        )
        data = YamlBookLoader(tmp_path).load()
        assert len(data.knowledge_nodes) == 2

    def test_multiple_sentence_files_merged(self, tmp_path):
        """Multiple YAML files in sentences/ are merged."""
        sections = tmp_path / "sections.yaml"
        sections.write_text(
            'sections:\n  - id: "S1"\n    book: "Test"\n    title: "S"\n'
            '    pages: "p.1"\n    type: "grammar_lecture"\n'
            "section_knowledge_nodes: []\nsection_prerequisites: []\n"
        )
        sn_dir = tmp_path / "sentences"
        sn_dir.mkdir()
        (sn_dir / "a.yaml").write_text(
            'sentences:\n  - id: "s1"\n    section_id: "S1"\n'
            "    drill: 0\n    number: 1\n"
            '    role: "example"\n    english: "A"\n    japanese: "A"\n    notes: ""\n'
        )
        (sn_dir / "b.yaml").write_text(
            'sentences:\n  - id: "s2"\n    section_id: "S1"\n'
            "    drill: 0\n    number: 2\n"
            '    role: "example"\n    english: "B"\n    japanese: "B"\n    notes: ""\n'
        )
        data = YamlBookLoader(tmp_path).load()
        assert len(data.sentences) == 2
