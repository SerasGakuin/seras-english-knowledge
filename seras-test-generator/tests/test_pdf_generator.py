"""Tests for pdf_generator."""

from app.models import (
    KnowledgeQuestion,
    NodeSection,
    ReviewGuide,
    SentenceQuestion,
    TestData,
    WarmupQuestion,
)
from app.services.pdf_generator import (
    render_combined_html,
    generate_combined_pdf,
)


def _sample_test_data() -> TestData:
    return TestData(
        sections=["Ch01_01"],
        sections_label="Ch01_01〜Ch01_01",
        warmup_questions=[
            WarmupQuestion(
                number=1,
                question="5文型を全部言って",
                answer="SV, SVC, SVO, SVO1O2, SVOC",
                node_id="strc-002",
                node_name="5文型の定義",
                reference_pages="p.6",
                note="この知識は今回の範囲の前提です。不安なら先に p.6 を復習しましょう。",
            ),
        ],
        node_sections=[
            NodeSection(
                section_number=1,
                node_id="strc-007",
                node_name="5文型の意味",
                reference_pages="p.8",
                knowledge_questions=[
                    KnowledgeQuestion(
                        number=1,
                        question="第2文型の意味を全部言って",
                        answer="Cである/Cに感じる/Cのままだ/Cになる",
                        node_id="strc-007",
                        node_name="5文型の意味",
                        reference_pages="p.8",
                    ),
                ],
                sentence_questions=[
                    SentenceQuestion(
                        number=2,
                        english="The students in the classroom are very noisy.",
                        japanese="その教室にいる生徒たちは、とてもうるさい。",
                        structure="S M V C",
                        notes="in the classroomは前置詞+名詞",
                        knowledge_tags=("strc-008", "strc-009"),
                        focus_points=("Mの識別方法", "形容詞の2つの役割と文型判別への応用"),
                        source_pages="p.8-11",
                        source_section="Ch01_01",
                    ),
                ],
                review_guide=[
                    ReviewGuide(
                        node_id="strc-001",
                        node_name="主要素（S・V・O・C）の定義",
                        reference_pages="p.6",
                        reason="前提知識",
                    ),
                ],
            ),
        ],
        generated_at="2026-02-12T10:00:00Z",
    )


class TestRenderCombinedHTML:
    def test_renders_warmup(self) -> None:
        html = render_combined_html(_sample_test_data())
        assert "ウォームアップ" in html
        assert "5文型を全部言って" in html

    def test_renders_node_sections(self) -> None:
        html = render_combined_html(_sample_test_data())
        assert "セクション 1" in html
        assert "5文型の意味" in html
        assert "第2文型の意味を全部言って" in html

    def test_renders_focus_points(self) -> None:
        html = render_combined_html(_sample_test_data())
        assert "着眼点" in html
        assert "Mの識別方法" in html

    def test_renders_sentence_in_section(self) -> None:
        html = render_combined_html(_sample_test_data())
        assert "The students in the classroom" in html
        assert "構造" in html

    def test_renders_answer_in_same_html(self) -> None:
        html = render_combined_html(_sample_test_data())
        assert "解答" in html
        assert "Cである/Cに感じる" in html

    def test_renders_review_guide(self) -> None:
        html = render_combined_html(_sample_test_data())
        assert "この問題が解けなかった場合" in html
        assert "主要素" in html
        assert "前提知識" in html

    def test_renders_warmup_answer(self) -> None:
        html = render_combined_html(_sample_test_data())
        assert "ウォームアップ 解答" in html
        assert "SV, SVC, SVO" in html

    def test_header_has_range_and_date(self) -> None:
        html = render_combined_html(_sample_test_data())
        assert "Ch01_01〜Ch01_01" in html
        assert "2026-02-12" in html

    def test_has_page_break(self) -> None:
        html = render_combined_html(_sample_test_data())
        assert "page-break-before" in html

    def test_has_both_headers(self) -> None:
        html = render_combined_html(_sample_test_data())
        assert "確認テスト<" in html or ">確認テスト<" in html
        assert "確認テスト【解答・解説】" in html


class TestGeneratePDF:
    def test_combined_pdf_bytes_valid(self) -> None:
        pdf = generate_combined_pdf(_sample_test_data())
        assert pdf[:5] == b"%PDF-"
