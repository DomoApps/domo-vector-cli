import pytest
import argparse
import sys
from unittest.mock import patch, MagicMock

from domo_vector_cli import constants, main


def test_parse_args_upload_nodes_defaults(monkeypatch):
    test_args = ["main.py", "upload-nodes"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = main.parse_args()
    assert args.command == "upload-nodes"
    assert args.root == "./documentation"
    assert args.index_id == "partner-gpt-index"
    assert args.dry_run is False
    assert args.chunk_size == 1500
    assert args.overlap == constants.DEFAULT_CHUNK_OVERLAP


def test_parse_args_delete_by_id(monkeypatch):
    test_args = [
        "main.py",
        "delete-by-id",
        "--index-id",
        "foo",
        "--node-ids",
        "id1",
        "id2",
    ]
    monkeypatch.setattr(sys, "argv", test_args)
    args = main.parse_args()
    assert args.command == "delete-by-id"
    assert args.index_id == "foo"
    assert args.node_ids == ["id1", "id2"]


def test_add_delete_cli_commands_creates_parsers():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    main.add_delete_cli_commands(subparsers)
    # Check that the subparsers exist
    commands = ["delete-all", "delete-by-id", "delete-by-group"]
    for cmd in commands:
        assert cmd in subparsers.choices


def test_add_get_cli_commands_creates_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    main.add_get_cli_commands(subparsers)
    assert "get-all" in subparsers.choices


# You can add more tests for cli_main, but it requires more mocking of async and side effects.
