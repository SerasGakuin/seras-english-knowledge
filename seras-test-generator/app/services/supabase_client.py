"""Supabase REST client singleton (via postgrest-py)."""

from functools import lru_cache

from postgrest import SyncPostgrestClient


@lru_cache(maxsize=1)
def get_supabase_client() -> SyncPostgrestClient:
    """Return a cached PostgREST client pointing at Supabase."""
    from app.config import get_settings

    settings = get_settings()
    return SyncPostgrestClient(
        base_url=f"{settings.supabase_url}/rest/v1",
        headers={
            "apikey": settings.supabase_key,
            "Authorization": f"Bearer {settings.supabase_key}",
        },
    )
