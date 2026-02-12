"""Google Drive PDF uploader."""

import json
from typing import Any

from app.models import DriveUploadError


class DriveUploader:
    """Uploads PDFs to Google Drive and returns shareable links."""

    def __init__(self, service: Any, folder_id: str) -> None:
        self._service = service
        self._folder_id = folder_id

    @classmethod
    def from_env(cls) -> "DriveUploader":
        """Create uploader from environment variables."""
        from app.config import get_settings
        settings = get_settings()

        if not settings.google_service_account_json:
            raise DriveUploadError(detail="GOOGLE_SERVICE_ACCOUNT_JSON not configured")
        if not settings.google_drive_folder_id:
            raise DriveUploadError(detail="GOOGLE_DRIVE_FOLDER_ID not configured")

        from google.oauth2 import service_account
        from googleapiclient.discovery import build

        credentials = service_account.Credentials.from_service_account_info(
            json.loads(settings.google_service_account_json),
            scopes=["https://www.googleapis.com/auth/drive.file"],
        )
        service = build("drive", "v3", credentials=credentials)
        return cls(service, settings.google_drive_folder_id)

    def upload(self, pdf_bytes: bytes, filename: str) -> str:
        """Upload PDF bytes and return a viewer URL."""
        from googleapiclient.http import MediaInMemoryUpload

        try:
            media = MediaInMemoryUpload(pdf_bytes, mimetype="application/pdf")
            file_metadata = {
                "name": filename,
                "parents": [self._folder_id],
            }
            created = (
                self._service.files()
                .create(body=file_metadata, media_body=media, fields="id")
                .execute()
            )
            file_id = created["id"]

            self._service.permissions().create(
                fileId=file_id,
                body={"type": "anyone", "role": "reader"},
            ).execute()

            return f"https://drive.google.com/file/d/{file_id}/view"
        except Exception as e:
            raise DriveUploadError(detail=f"Failed to upload to Drive: {e}") from e
