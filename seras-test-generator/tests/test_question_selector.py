"""Tests for question_selector."""

from app.models import CheckPoint, KnowledgeNode
from app.services.data_loader import DataStore
from app.services.question_selector import (
    _assign_sentences_to_nodes,
    _build_review_guide,
    build_node_sections,
    build_test_data,
    parse_check_point,
    select_warmup_questions,
)


def _node(
    id: str = "test-001",
    name: str = "Test Node",
    priority: str = "P1",
    check_points: tuple[CheckPoint, ...] = (),
    understanding_goals: tuple[str, ...] = (),
    prerequisites: tuple[str, ...] = (),
) -> KnowledgeNode:
    return KnowledgeNode(
        id=id,
        name=name,
        category="test",
        priority=priority,
        prerequisites=prerequisites,
        understanding_goals=understanding_goals,
        check_points=check_points,
        references={"book": {"pages": "p.1"}},
        notes="",
    )


class TestParseCheckPoint:
    def test_question_answer(self) -> None:
        cp = CheckPoint(question="Cになれる品詞は？", answer="形容詞と名詞")
        q, a = parse_check_point(cp, ())
        assert q == "Cになれる品詞は？"
        assert a == "形容詞と名詞"

    def test_long_answer(self) -> None:
        cp = CheckPoint(question="OとCの違いは？", answer="Oは名詞のみ、Cは形容詞も可。CはS/Oとイコール関係")
        q, a = parse_check_point(cp, ())
        assert q == "OとCの違いは？"
        assert "名詞のみ" in a

    def test_with_english(self) -> None:
        cp = CheckPoint(question="The machine he inventedの関係代名詞は？", answer="目的格の関係代名詞が省略されている")
        q, a = parse_check_point(cp, ())
        assert "The machine" in q
        assert "目的格" in a

    def test_assessment_with_goals(self) -> None:
        cp = CheckPoint(question="S・V・O・Cそれぞれの品詞を即答できるか", answer="")
        goals = ("S=名詞、V=動詞、O=名詞、C=形容詞または名詞",)
        q, a = parse_check_point(cp, goals)
        assert q == "S・V・O・Cそれぞれの品詞を即答できるか"
        assert a == goals[0]

    def test_assessment_no_goals(self) -> None:
        cp = CheckPoint(question="何かを理解している", answer="")
        q, a = parse_check_point(cp, ())
        assert q == "何かを理解している"
        assert a == ""


class TestSelectWarmupQuestions:
    def test_finds_outside_prereqs(self, data_store: DataStore) -> None:
        # strc-007 has prerequisite strc-002, which is outside target set
        warmup = select_warmup_questions({"strc-007"}, data_store)
        warmup_ids = {q.node_id for q in warmup}
        assert "strc-002" in warmup_ids

    def test_respects_max(self, data_store: DataStore) -> None:
        warmup = select_warmup_questions({"strc-007"}, data_store, target_max=2)
        assert len(warmup) <= 2

    def test_no_duplicates(self, data_store: DataStore) -> None:
        warmup = select_warmup_questions({"strc-007", "strc-008", "strc-009"}, data_store)
        ids_and_qs = [(q.node_id, q.question) for q in warmup]
        assert len(ids_and_qs) == len(set(ids_and_qs))

    def test_empty_when_no_prereqs(self, data_store: DataStore) -> None:
        # strc-001 has no prerequisites
        warmup = select_warmup_questions({"strc-001"}, data_store)
        assert warmup == []

    def test_numbering_starts_at_1(self, data_store: DataStore) -> None:
        warmup = select_warmup_questions({"strc-007"}, data_store)
        if warmup:
            assert warmup[0].number == 1

    def test_note_contains_reference(self, data_store: DataStore) -> None:
        warmup = select_warmup_questions({"strc-007"}, data_store)
        for q in warmup:
            assert "復習" in q.note


class TestAssignSentencesToNodes:
    def test_assigns_to_matching_node(self, data_store: DataStore) -> None:
        nodes = []
        for nid in ["strc-007", "strc-008", "strc-009"]:
            n = data_store.get_node(nid)
            if n:
                nodes.append(n)
        result = _assign_sentences_to_nodes(["Ch01_01"], nodes, data_store)
        # strc-008 tagged sentences should go to strc-008
        assert len(result) > 0
        # At least one node should have sentences
        total = sum(len(sqs) for sqs in result.values())
        assert total > 0

    def test_practice_only(self, data_store: DataStore) -> None:
        nodes = []
        for nid in ["strc-007", "strc-008", "strc-009"]:
            n = data_store.get_node(nid)
            if n:
                nodes.append(n)
        result = _assign_sentences_to_nodes(["Ch01_01"], nodes, data_store)
        for sqs in result.values():
            for sq in sqs:
                # Example sentence should not appear
                assert sq.english != "The old woman lives quietly in the countryside."

    def test_max_one_per_node(self, data_store: DataStore) -> None:
        nodes = []
        for nid in ["strc-007", "strc-008", "strc-009"]:
            n = data_store.get_node(nid)
            if n:
                nodes.append(n)
        result = _assign_sentences_to_nodes(["Ch01_01"], nodes, data_store)
        for sqs in result.values():
            assert len(sqs) <= 1

    def test_focus_points_populated(self, data_store: DataStore) -> None:
        nodes = []
        for nid in ["strc-007", "strc-008", "strc-009"]:
            n = data_store.get_node(nid)
            if n:
                nodes.append(n)
        result = _assign_sentences_to_nodes(["Ch01_01"], nodes, data_store)
        for sqs in result.values():
            for sq in sqs:
                assert len(sq.focus_points) > 0

    def test_introduction_skipped(self, data_store: DataStore) -> None:
        node = data_store.get_node("strc-001")
        assert node is not None
        result = _assign_sentences_to_nodes(["Ch01_00"], [node], data_store)
        assert result == {}


class TestBuildNodeSections:
    def test_creates_sections_per_node(self, data_store: DataStore) -> None:
        nodes = []
        for nid in ["strc-007", "strc-008", "strc-009"]:
            n = data_store.get_node(nid)
            if n:
                nodes.append(n)
        target_ids = {n.id for n in nodes}
        sentence_map = _assign_sentences_to_nodes(["Ch01_01"], nodes, data_store)
        sections = build_node_sections(nodes, sentence_map, target_ids, data_store)
        assert len(sections) == len(nodes)

    def test_section_numbering(self, data_store: DataStore) -> None:
        nodes = []
        for nid in ["strc-007", "strc-008", "strc-009"]:
            n = data_store.get_node(nid)
            if n:
                nodes.append(n)
        target_ids = {n.id for n in nodes}
        sentence_map = _assign_sentences_to_nodes(["Ch01_01"], nodes, data_store)
        sections = build_node_sections(nodes, sentence_map, target_ids, data_store)
        for i, sec in enumerate(sections):
            assert sec.section_number == i + 1

    def test_knowledge_questions_limited(self, data_store: DataStore) -> None:
        nodes = []
        for nid in ["strc-007", "strc-008"]:
            n = data_store.get_node(nid)
            if n:
                nodes.append(n)
        target_ids = {n.id for n in nodes}
        sections = build_node_sections(nodes, {}, target_ids, data_store, max_checks_per_node=2)
        for sec in sections:
            assert len(sec.knowledge_questions) <= 2

    def test_empty_sentence_node(self, data_store: DataStore) -> None:
        # Node with no sentences assigned
        node = data_store.get_node("strc-002")
        assert node is not None
        target_ids = {node.id}
        sections = build_node_sections([node], {}, target_ids, data_store)
        assert len(sections) == 1
        assert sections[0].sentence_questions == []


class TestBuildReviewGuide:
    def test_includes_prereqs(self, data_store: DataStore) -> None:
        from app.models import SentenceQuestion
        sq = SentenceQuestion(
            number=1,
            english="test",
            japanese="テスト",
            structure="S V",
            notes="",
            knowledge_tags=("strc-008",),
            focus_points=("Mの識別方法",),
            source_pages="p.8",
            source_section="Ch01_01",
        )
        guides = _build_review_guide([sq], {"strc-007", "strc-008", "strc-009"}, data_store)
        guide_ids = {g.node_id for g in guides}
        # strc-008 prereqs strc-002, which should appear as review guide
        assert "strc-002" in guide_ids

    def test_empty_when_no_sentences(self, data_store: DataStore) -> None:
        guides = _build_review_guide([], {"strc-007"}, data_store)
        assert guides == []

    def test_prereq_reason(self, data_store: DataStore) -> None:
        from app.models import SentenceQuestion
        sq = SentenceQuestion(
            number=1,
            english="test",
            japanese="テスト",
            structure="S V",
            notes="",
            knowledge_tags=("strc-008",),
            focus_points=("Mの識別方法",),
            source_pages="p.8",
            source_section="Ch01_01",
        )
        guides = _build_review_guide([sq], {"strc-008"}, data_store)
        prereq_guides = [g for g in guides if g.node_id == "strc-002"]
        assert len(prereq_guides) == 1
        assert prereq_guides[0].reason == "前提知識"


class TestBuildTestData:
    def test_assembles_all_components(self, data_store: DataStore) -> None:
        td = build_test_data(["Ch01_00", "Ch01_01"], data_store)
        assert td.sections == ["Ch01_00", "Ch01_01"]
        assert len(td.node_sections) > 0
        assert td.generated_at != ""

    def test_sections_label(self, data_store: DataStore) -> None:
        td = build_test_data(["Ch01_00", "Ch01_01"], data_store)
        assert td.sections_label == "Ch01_00〜Ch01_01"

    def test_warmup_present(self, data_store: DataStore) -> None:
        td = build_test_data(["Ch01_00", "Ch01_01"], data_store)
        # strc-007 has prerequisite strc-002, which should generate warmup
        assert len(td.warmup_questions) > 0

    def test_continuous_numbering(self, data_store: DataStore) -> None:
        td = build_test_data(["Ch01_00", "Ch01_01"], data_store)
        # Collect all question numbers from node sections
        numbers: list[int] = []
        for ns in td.node_sections:
            for kq in ns.knowledge_questions:
                numbers.append(kq.number)
            for sq in ns.sentence_questions:
                numbers.append(sq.number)
        # Should be continuous
        assert numbers == list(range(1, len(numbers) + 1))

    def test_node_sections_have_knowledge_questions(self, data_store: DataStore) -> None:
        td = build_test_data(["Ch01_00", "Ch01_01"], data_store)
        for ns in td.node_sections:
            assert len(ns.knowledge_questions) > 0
