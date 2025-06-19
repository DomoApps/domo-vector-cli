import argparse
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from domo_vector_cli.main import add_vector_cli_commands
from domo_vector_cli import get
import pytest
import asyncio


def test_add_get_cli_commands_creates_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    add_vector_cli_commands(subparsers)
    assert "vector" in subparsers.choices
    vector_parser = subparsers.choices["vector"]
    vector_subparsers = None
    for action in vector_parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            vector_subparsers = action
            break
    assert vector_subparsers is not None
    assert "get-all" in vector_subparsers.choices


@pytest.mark.asyncio
async def test_get_all_node_ids(monkeypatch):
    # Arrange
    async def mock_post(url, json, headers):
        class MockResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return {"nodes": [{"id": "id1"}, {"id": "id2"}, {"id": "id3"}]}

        return MockResponse()

    class MockAsyncClient:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        async def post(self, url, json, headers):
            return await mock_post(url, json, headers)

    monkeypatch.setattr("httpx.AsyncClient", lambda: MockAsyncClient())
    # Act
    result = await get.get_all_node_ids("test-index")
    # Assert
    assert result == ["id1", "id2", "id3"]
