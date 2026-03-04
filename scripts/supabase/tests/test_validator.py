"""Tests for pre-insert validation."""

from pathlib import Path

from book_importer.loader import YamlBookLoader
from book_importer.types import BookData, ValidationError
from book_importer.validator import ImportValidator

FIXTURES = Path(__file__).parent / "fixtures"


def _make_data(**overrides) -> BookData:
    """Build a minimal valid BookData with optional overrides."""
    defaults = dict(
        book_name="Test",
        knowledge_nodes=[{"id": "n1"}, {"id": "n2"}],
        understanding_goals=[{"node_id": "n1", "goal": "G", "seq": 1}],
        check_points=[{"node_id": "n1", "point": "C", "seq": 1}],
        node_prerequisites=[{"node_id": "n2", "prerequisite_id": "n1"}],
        knowledge_references=[{"node_id": "n1", "reference": "R", "seq": 1}],
        sections=[
            {"id": "S1", "book": "Test", "title": "S", "pages": "p.1", "type": "grammar_lecture"}
        ],
        section_knowledge_nodes=[{"section_id": "S1", "node_id": "n1", "seq": 1}],
        section_prerequisites=[],
        sentences=[
            {"id": "s1", "section_id": "S1", "drill": 0, "number": 1,
             "role": "example", "english": "A", "japanese": "B", "notes": ""}
        ],
        sentence_structures=[{"sentence_id": "s1", "label": "S", "content": "A", "seq": 1}],
        sentence_knowledge_tags=[{"sentence_id": "s1", "node_id": "n1"}],
    )
    defaults.update(overrides)
    return BookData(**defaults)


class TestValidDataPasses:
    def test_fixture_data_is_valid(self):
        data = YamlBookLoader(FIXTURES).load()
        errors = ImportValidator().validate(data)
        assert errors == []

    def test_minimal_valid_data(self):
        data = _make_data()
        errors = ImportValidator().validate(data)
        assert errors == []


class TestEmptyDataDetection:
    def test_empty_nodes_is_error(self):
        data = _make_data(knowledge_nodes=[])
        errors = ImportValidator().validate(data)
        assert any("knowledge_nodes" in str(e) and "empty" in str(e).lower() for e in errors)

    def test_empty_sections_is_error(self):
        data = _make_data(sections=[])
        errors = ImportValidator().validate(data)
        assert any("sections" in str(e) and "empty" in str(e).lower() for e in errors)

    def test_empty_book_name_is_error(self):
        data = _make_data(book_name="")
        errors = ImportValidator().validate(data)
        assert any("book_name" in str(e) for e in errors)


class TestDuplicateIdDetection:
    def test_duplicate_node_ids(self):
        data = _make_data(knowledge_nodes=[{"id": "n1"}, {"id": "n1"}])
        errors = ImportValidator().validate(data)
        assert any("duplicate" in str(e).lower() and "n1" in str(e) for e in errors)

    def test_duplicate_section_ids(self):
        data = _make_data(sections=[
            {"id": "S1", "book": "T", "title": "S", "pages": "p.1", "type": "grammar_lecture"},
            {"id": "S1", "book": "T", "title": "S", "pages": "p.2", "type": "grammar_lecture"},
        ])
        errors = ImportValidator().validate(data)
        assert any("duplicate" in str(e).lower() and "S1" in str(e) for e in errors)

    def test_duplicate_sentence_ids(self):
        data = _make_data(sentences=[
            {"id": "s1", "section_id": "S1", "drill": 0, "number": 1,
             "role": "example", "english": "A", "japanese": "B", "notes": ""},
            {"id": "s1", "section_id": "S1", "drill": 0, "number": 2,
             "role": "example", "english": "C", "japanese": "D", "notes": ""},
        ])
        errors = ImportValidator().validate(data)
        assert any("duplicate" in str(e).lower() and "s1" in str(e) for e in errors)


class TestForeignKeyValidation:
    def test_goal_references_missing_node(self):
        data = _make_data(understanding_goals=[{"node_id": "missing", "goal": "G", "seq": 1}])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) and "understanding_goals" in str(e) for e in errors)

    def test_checkpoint_references_missing_node(self):
        data = _make_data(check_points=[{"node_id": "missing", "point": "C", "seq": 1}])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) and "check_points" in str(e) for e in errors)

    def test_node_prereq_references_missing_node(self):
        data = _make_data(node_prerequisites=[{"node_id": "missing", "prerequisite_id": "n1"}])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)

    def test_node_prereq_references_missing_prerequisite(self):
        data = _make_data(node_prerequisites=[{"node_id": "n1", "prerequisite_id": "missing"}])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)

    def test_knowledge_ref_references_missing_node(self):
        data = _make_data(knowledge_references=[{"node_id": "missing", "reference": "R", "seq": 1}])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)

    def test_section_kn_references_missing_section(self):
        data = _make_data(section_knowledge_nodes=[
            {"section_id": "missing", "node_id": "n1", "seq": 1}
        ])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)

    def test_section_kn_references_missing_node(self):
        data = _make_data(section_knowledge_nodes=[
            {"section_id": "S1", "node_id": "missing", "seq": 1}
        ])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)

    def test_section_prereq_references_missing_section(self):
        data = _make_data(section_prerequisites=[
            {"section_id": "missing", "prerequisite_id": "S1"}
        ])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)

    def test_section_prereq_references_missing_prerequisite(self):
        data = _make_data(section_prerequisites=[
            {"section_id": "S1", "prerequisite_id": "missing"}
        ])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)

    def test_sentence_references_missing_section(self):
        data = _make_data(sentences=[
            {"id": "s1", "section_id": "missing", "drill": 0, "number": 1,
             "role": "example", "english": "A", "japanese": "B", "notes": ""}
        ])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)

    def test_structure_references_missing_sentence(self):
        data = _make_data(sentence_structures=[
            {"sentence_id": "missing", "label": "S", "content": "A", "seq": 1}
        ])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)

    def test_tag_references_missing_sentence(self):
        data = _make_data(sentence_knowledge_tags=[
            {"sentence_id": "missing", "node_id": "n1"}
        ])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)

    def test_tag_references_missing_node(self):
        data = _make_data(sentence_knowledge_tags=[
            {"sentence_id": "s1", "node_id": "missing"}
        ])
        errors = ImportValidator().validate(data)
        assert any("missing" in str(e) for e in errors)
