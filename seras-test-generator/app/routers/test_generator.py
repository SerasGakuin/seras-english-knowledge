"""POST /generate-test endpoint."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends

from app.models import (
    GenerateTestRequest,
    GenerateTestResponse,
    TestMetadata,
)
from app.services.data_loader import DataStore, get_data_store
from app.services.drive_uploader import DriveUploader
from app.services.pdf_generator import generate_answer_pdf, generate_test_pdf
from app.services.question_selector import build_test_data
from app.services.section_parser import parse_sections

router = APIRouter()


@router.post("/generate-test", response_model=GenerateTestResponse)
async def generate_test(
    request: GenerateTestRequest,
    data_store: DataStore = Depends(get_data_store),
) -> GenerateTestResponse:
    section_ids = parse_sections(request.sections, data_store)
    test_data = build_test_data(section_ids, data_store)

    test_pdf = generate_test_pdf(test_data)
    answer_pdf = generate_answer_pdf(test_data)

    uploader = DriveUploader.from_env()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    range_str = test_data.sections_label
    test_url = uploader.upload(test_pdf, f"確認テスト_{range_str}_{timestamp}.pdf")
    answer_url = uploader.upload(
        answer_pdf, f"確認テスト_解答_{range_str}_{timestamp}.pdf"
    )

    # Collect all knowledge node IDs used
    node_ids = sorted(
        {ns.node_id for ns in test_data.node_sections}
    )

    # Count questions
    question_count = sum(
        len(ns.knowledge_questions) for ns in test_data.node_sections
    )
    sentence_count = sum(
        len(ns.sentence_questions) for ns in test_data.node_sections
    )

    return GenerateTestResponse(
        pdf_url=test_url,
        answer_pdf_url=answer_url,
        metadata=TestMetadata(
            sections=test_data.sections,
            knowledge_nodes_used=node_ids,
            question_count=question_count,
            sentence_count=sentence_count,
            warmup_count=len(test_data.warmup_questions),
            generated_at=test_data.generated_at,
        ),
    )
