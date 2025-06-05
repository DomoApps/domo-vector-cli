import pytest
import argparse
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import add_delete_cli_commands


def test_add_delete_cli_commands_creates_parsers():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    add_delete_cli_commands(subparsers)
    commands = ["delete-all", "delete-by-id", "delete-by-group"]
    for cmd in commands:
        assert cmd in subparsers.choices
