def handle_help_cli(*args, **kwargs):
    """
    Print the help message for the CLI.
    """
    print("\nUsage: domo-vector <command> [options]\n")
    print("Commands:")
    print("  vector                 Manage vector index nodes (upload, delete, get)")
    print("    upload               Chunk and upload files as nodes")
    print("                         Use --global flag to upload to global indexes")
    print("    delete-all           Delete all nodes in the index")
    print("    delete-by-id         Delete nodes by nodeId")
    print("    delete-by-group      Delete nodes by nodeGroupId (groupId)")
    print("    get-all              Fetch all node IDs from the specified index\n")
    print("  fileset                Manage filesets")
    print("    create               Create a new fileset")
    print("    upload-file          Upload a file or directory to a fileset")
    print("    get-file             Get a file from a fileset")
    print("    get-fileset          Get a fileset by ID")
    print("    get-filesets         List all filesets")
    print(
        "    search-filesets      List/search filesets (with optional sort, filters, pagination)\n"
    )
    print("  help                   Show this help message and exit\n")
    print("Use 'domo-vector <command> --help' for more information on a command.")
