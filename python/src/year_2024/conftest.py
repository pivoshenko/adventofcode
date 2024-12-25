"""Module that contains fixtures for the tests."""

from __future__ import annotations

import pathlib

import pytest


@pytest.fixture
def examples_dir() -> pathlib.Path:
    repository_root_dir = pathlib.Path(__file__).parent.parent.parent.parent

    return repository_root_dir / "data" / "examples" / "year_2024"
