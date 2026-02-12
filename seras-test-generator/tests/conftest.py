"""Shared test fixtures."""

from pathlib import Path

import pytest

from app.services.data_loader import DataStore

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def data_store() -> DataStore:
    return DataStore(FIXTURES_DIR)
