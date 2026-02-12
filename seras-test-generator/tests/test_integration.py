"""Integration tests for the full API flow."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.data_loader import DataStore, get_data_store

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def _fixture_data_store() -> DataStore:
    return DataStore(FIXTURES_DIR)


@pytest.fixture
def client() -> TestClient:  # type: ignore[misc]
    app.dependency_overrides[get_data_store] = _fixture_data_store
    yield TestClient(app)
    app.dependency_overrides.clear()


def _mock_uploader() -> MagicMock:
    mock = MagicMock()
    mock.upload.return_value = "https://storage.googleapis.com/seras-test-pdfs/test123.pdf"
    return mock


class TestIntegration:
    @patch("app.routers.test_generator.GCSUploader")
    def test_full_flow_200(self, mock_cls: MagicMock, client: TestClient) -> None:
        mock_cls.from_env.return_value = _mock_uploader()
        response = client.post(
            "/generate-test", json={"sections": "1-0~1-1"}
        )
        assert response.status_code == 200

    @patch("app.routers.test_generator.GCSUploader")
    def test_response_has_urls(self, mock_cls: MagicMock, client: TestClient) -> None:
        mock_cls.from_env.return_value = _mock_uploader()
        response = client.post(
            "/generate-test", json={"sections": "1-0~1-1"}
        )
        data = response.json()
        assert "pdf_url" in data
        assert "answer_pdf_url" in data
        assert data["pdf_url"].startswith("https://")

    @patch("app.routers.test_generator.GCSUploader")
    def test_metadata_sections(self, mock_cls: MagicMock, client: TestClient) -> None:
        mock_cls.from_env.return_value = _mock_uploader()
        response = client.post(
            "/generate-test", json={"sections": "1-0~1-1"}
        )
        data = response.json()
        assert data["metadata"]["sections"] == ["Ch01_00", "Ch01_01"]
        assert data["metadata"]["question_count"] > 0
        assert "warmup_count" in data["metadata"]

    def test_invalid_section_400(self, client: TestClient) -> None:
        response = client.post(
            "/generate-test", json={"sections": "abc"}
        )
        assert response.status_code == 400

    def test_empty_sections_400(self, client: TestClient) -> None:
        response = client.post(
            "/generate-test", json={"sections": ""}
        )
        assert response.status_code == 400
