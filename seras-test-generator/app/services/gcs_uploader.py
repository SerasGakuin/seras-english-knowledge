"""Google Cloud Storage PDF uploader."""

from app.models import DriveUploadError


class GCSUploader:
    """Uploads PDFs to GCS and returns public URLs."""

    def __init__(self, bucket_name: str) -> None:
        from google.cloud import storage

        self._client = storage.Client()
        self._bucket = self._client.bucket(bucket_name)

    @classmethod
    def from_env(cls) -> "GCSUploader":
        from app.config import get_settings

        bucket = get_settings().gcs_bucket_name
        if not bucket:
            raise DriveUploadError(detail="GCS_BUCKET_NAME not configured")
        return cls(bucket)

    def upload(self, pdf_bytes: bytes, filename: str) -> str:
        """Upload PDF bytes and return a public URL."""
        try:
            blob = self._bucket.blob(filename)
            blob.upload_from_string(pdf_bytes, content_type="application/pdf")
            return blob.public_url
        except Exception as e:
            raise DriveUploadError(detail=f"Failed to upload to GCS: {e}") from e
