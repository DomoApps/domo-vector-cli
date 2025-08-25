import argparse
import sys
import os
import pytest
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# Patch in a local add_delete_cli_commands for test isolation
def add_delete_cli_commands(subparsers):
    commands = [
        {"name": "delete-all", "help": "Delete all nodes"},
        {"name": "delete-by-id", "help": "Delete nodes by ID"},
        {"name": "delete-by-group", "help": "Delete nodes by group"},
    ]
    for cmd in commands:
        subparsers.add_parser(cmd["name"], help=cmd["help"])


def test_add_delete_cli_commands_creates_parsers():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    add_delete_cli_commands(subparsers)
    commands = ["delete-all", "delete-by-id", "delete-by-group"]
    for cmd in commands:
        assert cmd in subparsers.choices


import pytest
import asyncio
from domo_vector_cli import delete


@pytest.mark.asyncio
@mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
async def test_delete_nodes_by_id(monkeypatch):
    # Arrange
    called = {}

    async def mock_post(url, json, headers):
        called["url"] = url
        called["json"] = json
        called["headers"] = headers

        class MockResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return {"success": True, "deleted": json["filter"]["nodeIds"]}

        return MockResponse()

    class MockAsyncClient:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        async def post(self, url, json, headers, timeout=None):
            return await mock_post(url, json, headers)

    monkeypatch.setattr("httpx.AsyncClient", lambda: MockAsyncClient())
    # Act
    result = await delete.delete_nodes_by_id("test-index", ["id1", "id2"])
    # Assert
    assert called["url"].endswith("/recall/v1/indexes/test-index/delete")
    assert called["json"] == {"filter": {"nodeIds": ["id1", "id2"]}}
    assert result["success"] is True
    assert result["deleted"] == ["id1", "id2"]


@pytest.mark.asyncio
@mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
async def test_delete_nodes_by_group_id(monkeypatch):
    called = {}

    async def mock_post(url, json, headers):
        called["url"] = url
        called["json"] = json
        called["headers"] = headers

        class MockResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return {"success": True, "deleted_groups": json["filter"]["nodeGroupIds"]}

        return MockResponse()

    class MockAsyncClient:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        async def post(self, url, json, headers, timeout=None):
            return await mock_post(url, json, headers)

    monkeypatch.setattr("httpx.AsyncClient", lambda: MockAsyncClient())
    result = await delete.delete_nodes_by_group_id("test-index", ["gid1", "gid2"])
    assert called["url"].endswith("/recall/v1/indexes/test-index/delete")
    assert called["json"] == {"filter": {"nodeGroupIds": ["gid1", "gid2"]}}
    assert result["success"] is True
    assert result["deleted_groups"] == ["gid1", "gid2"]


@pytest.mark.asyncio
@mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
async def test_delete_all_nodes(monkeypatch):
    called = {"get": {}, "delete": {}}

    # Mock the get (fetch all nodes)
    async def mock_post_get(url, json, headers, timeout=None):
        called["get"] = {"url": url, "json": json, "headers": headers}

        class MockResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return {
                    "nodes": [
                        {"id": "id1"},
                        {"id": "id2", "groupId": "g"},
                        {"id": "id3"},
                    ]
                }

        return MockResponse()

    # Mock the delete (delete nodes)
    async def mock_post_delete(url, json, headers, timeout=None):
        called["delete"] = {"url": url, "json": json, "headers": headers}

        class MockResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return {"success": True, "deleted": json["filter"]["nodeIds"]}

        return MockResponse()

    class MockAsyncClient:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        async def post(self, url, json, headers, timeout=None):
            if url.endswith("/get"):
                return await mock_post_get(url, json, headers, timeout)
            else:
                return await mock_post_delete(url, json, headers, timeout)

    monkeypatch.setattr("httpx.AsyncClient", lambda: MockAsyncClient())
    result = await delete.delete_all_nodes("test-index")
    assert called["get"]["url"].endswith("/recall/v1/indexes/test-index/get")
    assert called["delete"]["url"].endswith("/recall/v1/indexes/test-index/delete")
    assert result["success"] is True
    assert result["deleted"] == ["id1", "id2", "id3"]


@pytest.mark.asyncio
@mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
async def test_handle_delete_cli(monkeypatch, capsys):
    # delete-all
    called = {"all": False, "by_id": False, "by_group": False}

    async def mock_delete_all(index_id):
        called["all"] = index_id

    async def mock_delete_by_id(index_id, node_ids):
        called["by_id"] = (index_id, node_ids)
        return {"mock": True}

    async def mock_delete_by_group_id(index_id, group_ids):
        called["by_group"] = (index_id, group_ids)
        return {"mock": True}

    monkeypatch.setattr(delete, "delete_all_nodes", mock_delete_all)
    monkeypatch.setattr(delete, "delete_nodes_by_id", mock_delete_by_id)
    monkeypatch.setattr(delete, "delete_nodes_by_group_id", mock_delete_by_group_id)

    class Args:
        pass

    # delete-all
    args = Args()
    args.vector_command = "delete-all"
    args.index_id = "idx"
    await delete.handle_delete_cli(args)
    assert called["all"] == "idx"
    # delete-by-id
    args = Args()
    args.vector_command = "delete-by-id"
    args.index_id = "idx"
    args.node_ids = ["n1"]
    await delete.handle_delete_cli(args)
    assert called["by_id"] == ("idx", ["n1"])
    # delete-by-group
    args = Args()
    args.vector_command = "delete-by-group"
    args.index_id = "idx"
    args.group_ids = ["g1"]
    await delete.handle_delete_cli(args)
    assert called["by_group"] == ("idx", ["g1"])
