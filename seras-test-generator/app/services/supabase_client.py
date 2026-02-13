"""Supabase client singleton."""

from functools import lru_cache

from supabase import Client, create_client


@lru_cache(maxsize=1)
def get_supabase_client() -> Client:
    """Return a cached Supabase client instance."""
    from app.config import get_settings

    settings = get_settings()
    return create_client(settings.supabase_url, settings.supabase_key)
