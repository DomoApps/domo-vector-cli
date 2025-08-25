import os
import argparse
import asyncio
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

    # Add configure command
    add_configure_command(subparsers)

    # Add help command
    add_help_command(subparsers)

    # Add fileset commands
    add_fileset_cli_commands(subparsers)

    # Add nodes commands
    add_vector_cli_commands(subparsers)

    return parser.parse_args()


async def cli_main():
    args = parse_args()
    # Always allow configure and help

    if args.command == "help" or args.command is None:
        handle_help_cli()
        return
    if args.command == "configure":
        handle_configure_cli()
        return

    # Check for required configuration
    from domo_vector_cli.config import config
    is_valid, error_type = config.validate_required_config()
    if not is_valid:
        if error_type == "no_env_file":
            print("\nSETUP REQUIRED: No configuration file found.")
            print("This appears to be your first time using domo-vector.")
            print("\nTo get started, run:")
            print("  domo-vector configure")
            print("\nThis will prompt you for your Domo credentials and create a .env file.")
        else:  # empty_config
            print("\nCONFIGURATION ERROR: Missing required credentials in .env file.")
            print("Your .env file exists but is missing required values:")
            print("  - DOMO_DEVELOPER_TOKEN")
            print("  - DOMO_API_URL_BASE")
            print("\nTo fix this, run:")
            print("  domo-vector configure")
        print()
        return
    elif args.command == "fileset":
        from domo_vector_cli.fileset import handle_fileset_cli

        await handle_fileset_cli(args)
    elif args.command == "vector":
        from domo_vector_cli.vector import handle_vector_cli

        await handle_vector_cli(args)


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


def add_vector_cli_commands(subparsers):
    from domo_vector_cli.constants import COMMANDS

    vector_cmd = COMMANDS["vector"]
    parser_nodes = subparsers.add_parser(vector_cmd["name"], help=vector_cmd["help"])
    nodes_subparsers = parser_nodes.add_subparsers(
        dest="vector_command", help="Vector subcommands"
    )

    for subcmd_name, subcmd in vector_cmd["subcommands"].items():
        parser_sub = nodes_subparsers.add_parser(subcmd_name, help=subcmd["help"])
        for arg in subcmd["args"]:
            kwargs = arg.copy()
            name = kwargs.pop("name")
            parser_sub.add_argument(name, **kwargs)
    parser_nodes.set_defaults(func=None)


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
