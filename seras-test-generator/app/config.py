"""Application settings."""

from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    data_dir: str = "../"
    google_service_account_json: str = ""
    google_drive_folder_id: str = ""
    gcs_bucket_name: str = ""
    port: int = 8080
    supabase_url: str = ""
    supabase_key: str = ""
    data_store_type: str = "yaml"  # "yaml" or "supabase"

    model_config = {"env_prefix": ""}


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
