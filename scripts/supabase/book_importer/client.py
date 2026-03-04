"""Supabase client helper."""

from __future__ import annotations

import os
import sys


def get_supabase_client():
    """Create a Supabase client from environment variables."""
    from supabase import create_client

    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        print("Error: SUPABASE_URL and SUPABASE_KEY must be set")
        sys.exit(1)
    return create_client(url, key)
