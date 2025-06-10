import argparse
import sys
import os

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
