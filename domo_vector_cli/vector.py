from domo_vector_cli.delete import handle_delete_cli
from domo_vector_cli.get import handle_get_cli
from domo_vector_cli.upsert import handle_upload_cli


async def handle_vector_cli(args):
    """Handle the vector CLI commands.  This function processes the vector commands
    and delegates to the appropriate handler based on the subcommand provided.
    """
    import os
    
    # Nested nodes subcommands
    if not hasattr(args, "vector_command") or args.vector_command is None:
        print(
            "Please specify a vector subcommand. Use 'domo-vector vector --help' for options."
        )
        return
    
    # Resolve index_id from environment if not provided
    if hasattr(args, 'index_id') and args.index_id is None:
        env_index_id = os.environ.get("VECTOR_INDEX_ID")
        if env_index_id:
            args.index_id = env_index_id
        else:
            print("\nERROR: No index ID specified.")
            print("Either provide --index-id or set VECTOR_INDEX_ID in your .env file.")
            print("Run 'domo-vector configure' to set up your .env file.")
            return
    if args.vector_command == "upload":
        await handle_upload_cli(args)
    elif args.vector_command == "delete-all":
        await handle_delete_cli(args)
    elif args.vector_command == "delete-by-id":
        await handle_delete_cli(args)
    elif args.vector_command == "delete-by-group":
        await handle_delete_cli(args)
    elif args.vector_command == "get-all":
        await handle_get_cli(args)
    else:
        print(f"Unknown nodes subcommand: {args.vector_command}")
