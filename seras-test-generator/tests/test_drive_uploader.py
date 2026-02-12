"""Tests for drive_uploader."""

from unittest.mock import MagicMock

import pytest

from app.models import DriveUploadError
from app.services.drive_uploader import DriveUploader


class TestDriveUploader:
    def test_upload_returns_url(self) -> None:
        mock_service = MagicMock()
        mock_service.files().create().execute.return_value = {"id": "abc123"}
        mock_service.permissions().create().execute.return_value = {}

        uploader = DriveUploader(mock_service, "folder_id")
        url = uploader.upload(b"%PDF-test", "test.pdf")

        assert "abc123" in url
        assert url == "https://drive.google.com/file/d/abc123/view"

    def test_sets_viewer_permission(self) -> None:
        mock_service = MagicMock()
        mock_service.files().create().execute.return_value = {"id": "abc123"}

        uploader = DriveUploader(mock_service, "folder_id")
        uploader.upload(b"%PDF-test", "test.pdf")

        mock_service.permissions().create.assert_called_once_with(
            fileId="abc123",
            body={"type": "anyone", "role": "reader"},
        )

    def test_upload_failure_raises(self) -> None:
        mock_service = MagicMock()
        mock_service.files().create().execute.side_effect = Exception("API error")

        uploader = DriveUploader(mock_service, "folder_id")
        with pytest.raises(DriveUploadError):
            uploader.upload(b"%PDF-test", "test.pdf")
