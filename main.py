import os
import argparse
import asyncio
from constants import DEFAULT_CHUNK_OVERLAP
from delete import handle_delete_cli
from get import handle_get_cli
from upsert import handle_upload_cli
from help import help
from dotenv import load_dotenv
from typing import List, Dict, Generator


load_dotenv()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Partner GPT Vector Index CLI",
        usage="python main.py <command> [options]",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Main (default) command for chunk/upload using COMMANDS
    from constants import COMMANDS

    cmd = COMMANDS["upload_nodes"]
    parser_main = subparsers.add_parser(cmd["name"], help=cmd["help"])
    for arg in cmd["args"]:
        kwargs = arg.copy()
        name = kwargs.pop("name")
        parser_main.add_argument(name, **kwargs)

    # Add delete commands
    add_delete_cli_commands(subparsers)

    # add get commands
    add_get_cli_commands(subparsers)

    return parser.parse_args()


async def cli_main():
    args = parse_args()
    if args.command == "help" or args.command is None:
        help()
    if args.command == "upload-nodes":
        await handle_upload_cli(args)
    elif args.command in ("delete-by-id", "delete-by-group", "delete-all"):
        await handle_delete_cli(args)
    elif args.command == "get-all":
        await handle_get_cli(args)


def add_delete_cli_commands(subparsers):
    from constants import COMMANDS

    for key in ["delete_all", "delete_by_id", "delete_by_group"]:
        cmd = COMMANDS[key]
        parser = subparsers.add_parser(cmd["name"], help=cmd["help"])
        for arg in cmd["args"]:
            kwargs = arg.copy()
            name = kwargs.pop("name")
            parser.add_argument(name, **kwargs)


def add_get_cli_commands(subparsers):
    # Get all node IDs
    parser_get_all = subparsers.add_parser(
        "get-all", help="Fetch all node IDs from the specified index"
    )
    parser_get_all.add_argument("--index-id", required=True, help="Index ID")
    parser_get_all.set_defaults(func=handle_get_cli)


if __name__ == "__main__":
    try:
        asyncio.run(cli_main())
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        import traceback

        print("\nAn unexpected error occurred:", str(e))
        traceback.print_exc()
