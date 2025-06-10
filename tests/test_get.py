import argparse
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from domo_vector_cli.main import add_get_cli_commands


def test_add_get_cli_commands_creates_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    add_get_cli_commands(subparsers)
    assert "get-all" in subparsers.choices
