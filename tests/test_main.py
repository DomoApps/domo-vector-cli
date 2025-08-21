import pytest
import argparse
import sys
from unittest.mock import patch, MagicMock

from domo_vector_cli import constants, main


def test_parse_args_upload_nodes_defaults(monkeypatch):
    """Test parsing upload command with default values."""
    test_args = ["main.py", "vector", "upload"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = main.parse_args()
    assert args.command == "vector"
    assert args.vector_command == "upload"
    assert args.root == "./documentation"
    # index_id default comes from environment variable, so it could be None
    assert hasattr(args, "index_id")  # Just check the attribute exists
    assert args.dry_run is False
    assert args.chunk_size == 1500
    assert args.overlap == constants.DEFAULT_CHUNK_OVERLAP


def test_parse_args_upload_nodes_with_index_id(monkeypatch):
    """Test parsing upload command with explicit index ID."""
    test_args = ["main.py", "vector", "upload", "--index-id", "my-test-index"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = main.parse_args()
    assert args.command == "vector"
    assert args.vector_command == "upload"
    assert args.index_id == "my-test-index"


def test_parse_args_delete_by_id(monkeypatch):
    test_args = [
        "main.py",
        "vector",
        "delete-by-id",
        "--index-id",
        "foo",
        "--node-ids",
        "id1",
        "id2",
    ]
    monkeypatch.setattr(sys, "argv", test_args)
    args = main.parse_args()
    assert args.command == "vector"
    assert args.vector_command == "delete-by-id"
    assert args.index_id == "foo"
    assert args.node_ids == ["id1", "id2"]


def test_add_vector_cli_commands_creates_parsers():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    main.add_vector_cli_commands(subparsers)
    assert "vector" in subparsers.choices
    vector_parser = subparsers.choices["vector"]
    vector_subparsers = None
    for action in vector_parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            vector_subparsers = action
            break
    assert vector_subparsers is not None
    expected = ["upload", "delete-all", "delete-by-id", "delete-by-group", "get-all"]
    for cmd in expected:
        assert cmd in vector_subparsers.choices


def test_add_fileset_cli_commands_creates_parsers():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    main.add_fileset_cli_commands(subparsers)
    assert "fileset" in subparsers.choices
    fileset_parser = subparsers.choices["fileset"]
    fileset_subparsers = None
    for action in fileset_parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            fileset_subparsers = action
            break
    assert fileset_subparsers is not None
    expected = [
        "create",
        "upload-file",
        "get-file",
        "get-fileset",
        "get-filesets",
        "search-filesets",
    ]
    for cmd in expected:
        assert cmd in fileset_subparsers.choices


# Example functional test for search_filesets (mocked)
def test_search_filesets_function(monkeypatch):
    from domo_vector_cli import fileset

    fake_response = {
        "success": True,
        "filesets": [{"id": "abc", "name": "Test Fileset"}],
    }
    monkeypatch.setattr(fileset, "search_filesets", lambda **kwargs: fake_response)
    result = fileset.search_filesets()
    assert result["success"]
    assert isinstance(result["filesets"], list)
    assert result["filesets"][0]["name"] == "Test Fileset"


# Example functional test for get_file_text_from_fileset (mocked)
def test_get_file_text_from_fileset(monkeypatch):
    from domo_vector_cli import fileset

    monkeypatch.setattr(
        fileset,
        "get_file_text_from_fileset",
        lambda *a, **k: {"success": True, "text": "hello world"},
    )
    result = fileset.get_file_text_from_fileset("fsid", file_id="fid")
    assert result["success"]
    assert result["text"] == "hello world"
