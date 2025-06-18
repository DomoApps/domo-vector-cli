import os
import argparse
import asyncio
from domo_vector_cli.delete import handle_delete_cli
from domo_vector_cli.get import handle_get_cli
from domo_vector_cli.upsert import handle_upload_cli
from domo_vector_cli.help import handle_help_cli
from domo_vector_cli.configure import handle_configure_cli
from dotenv import load_dotenv


load_dotenv()


def add_configure_command(subparsers):
    parser_configure = subparsers.add_parser(
        "configure", help="Configure your Domo URL and API key for the CLI"
    )
    parser_configure.set_defaults(func=handle_configure_cli)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Partner GPT Vector Index CLI",
        usage="domo-vector <command> [options]",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Main (default) command for chunk/upload using COMMANDS
    from domo_vector_cli.constants import COMMANDS

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

    # Add configure command
    add_configure_command(subparsers)

    # Add help command
    add_help_command(subparsers)

    # Add fileset commands
    add_fileset_cli_commands(subparsers)

    return parser.parse_args()


from domo_vector_cli.configure import handle_configure_cli


async def cli_main():
    args = parse_args()
    # Always allow configure and help

    if args.command == "help" or args.command is None:
        handle_help_cli()
        return
    if args.command == "configure":
        handle_configure_cli()
        return

    # Check for required environment variables
    token = os.environ.get("DOMO_DEVELOPER_TOKEN")
    url_base = os.environ.get("DOMO_API_URL_BASE")
    if not token or not url_base:
        print(
            "\nERROR: You must configure your DOMO_DEVELOPER_TOKEN and DOMO_API_URL_BASE before running this command."
        )
        print("Run: domo-vector configure\n")
        return

    if args.command == "upload-nodes":
        await handle_upload_cli(args)
    elif args.command in ("delete-by-id", "delete-by-group", "delete-all"):
        await handle_delete_cli(args)
    elif args.command == "get-all":
        await handle_get_cli(args)
    elif args.command == "fileset":
        from domo_vector_cli.fileset import handle_fileset_cli

        handle_fileset_cli(args)


def add_delete_cli_commands(subparsers):
    from domo_vector_cli.constants import COMMANDS

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


def add_help_command(subparsers):
    parser_help = subparsers.add_parser("help", help="Show this help message and exit")
    parser_help.set_defaults(func=handle_help_cli)


def add_fileset_cli_commands(subparsers):
    from domo_vector_cli.constants import COMMANDS

    fileset_cmd = COMMANDS["fileset"]
    parser_fileset = subparsers.add_parser(
        fileset_cmd["name"], help=fileset_cmd["help"]
    )
    fileset_subparsers = parser_fileset.add_subparsers(
        dest="fileset_command", help="Fileset subcommands"
    )

    for subcmd_name, subcmd in fileset_cmd["subcommands"].items():
        parser_sub = fileset_subparsers.add_parser(subcmd_name, help=subcmd["help"])
        for arg in subcmd["args"]:
            kwargs = arg.copy()
            name = kwargs.pop("name")
            parser_sub.add_argument(name, **kwargs)
    parser_fileset.set_defaults(func=None)


def main():
    try:
        asyncio.run(cli_main())
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        import traceback

        print("\nAn unexpected error occurred:", str(e))
        traceback.print_exc()


if __name__ == "__main__":
    main()
