"""Pytest fixtures for the FastAPI app tests."""
import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities state before and after each test."""
    original = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(original)


@pytest.fixture
def client():
    """Provide TestClient for the FastAPI app."""
    return TestClient(app_module.app)
