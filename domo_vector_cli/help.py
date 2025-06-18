def handle_help_cli(*args, **kwargs):
    """
    Print the help message for the CLI.
    """
    print("\nUsage: domo-vector <command> [options]\n")
    print("Commands:")
    print("  upload-nodes           Chunk and upload markdown files")
    print("  delete-all             Delete all nodes in the index")
    print("  delete-by-id           Delete nodes by nodeId")
    print("  delete-by-group        Delete nodes by nodeGroupId (groupId)")
    print("  get-all                Fetch all node IDs from the specified index")
    print("  configure              Configure the CLI with environment variables")
    print(
        "  fileset                Manage filesets (create, upload-file, get-file, get-fileset, get-filesets, search-filesets)"
    )
    print("  help                   Show this help message and exit\n")
    print("Use 'domo-vector <command> --help' for more information on a command.")
