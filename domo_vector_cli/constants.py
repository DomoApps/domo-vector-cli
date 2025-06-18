import os
from dotenv import load_dotenv

load_dotenv()
API_URL_BASE = os.environ.get("DOMO_API_URL_BASE", "https://domo-es.domo.com/api")
DEFAULT_CHUNK_SIZE = 1500
DEFAULT_CHUNK_OVERLAP = 200

COMMANDS = {
    "configure": {
        "name": "configure",
        "help": "Configure the CLI with environment variables",
    },
    "help": {
        "name": "help",
        "help": "Show this help message and exit",
    },
    "fileset": {
        "name": "fileset",
        "help": "Manage filesets (create, upload-file, get-file, get-fileset, get-filesets)",
        "subcommands": {
            "create": {
                "help": "Create a new fileset",
                "args": [
                    {"name": "--name", "required": True, "help": "Name of the fileset"},
                    {
                        "name": "--description",
                        "required": False,
                        "help": "Description of the fileset",
                    },
                ],
            },
            "upload-file": {
                "help": "Upload a file or directory to a fileset",
                "args": [
                    {
                        "name": "--fileset-id",
                        "required": True,
                        "help": "ID of the fileset",
                    },
                    {
                        "name": "--file-path",
                        "required": False,
                        "help": "Path to the file to upload",
                    },
                    {
                        "name": "--directory",
                        "required": False,
                        "help": "Path to the directory to upload (uploads all files recursively)",
                    },
                ],
            },
            "get-file": {
                "help": "Get a file from a fileset",
                "args": [
                    {
                        "name": "--fileset-id",
                        "required": True,
                        "help": "ID of the fileset",
                    },
                    {
                        "name": "--file-path",
                        "required": False,
                        "help": "Path of the file to retrieve",
                    },
                    {
                        "name": "--file-id",
                        "required": False,
                        "help": "ID of the file to retrieve",
                    },
                ],
            },
            "get-fileset": {
                "help": "Get a fileset by ID",
                "args": [
                    {
                        "name": "--fileset-id",
                        "required": True,
                        "help": "ID of the fileset",
                    }
                ],
            },
            "get-filesets": {"help": "List all filesets", "args": []},
            "search-filesets": {
                "help": "List/search filesets (with optional sort, filters, pagination)",
                "args": [
                    {
                        "name": "--limit",
                        "type": int,
                        "default": 10,
                        "help": "Max filesets to return",
                    },
                    {
                        "name": "--offset",
                        "type": int,
                        "default": 0,
                        "help": "Offset for pagination",
                    },
                ],
            },
        },
    },
    "vector": {
        "name": "vector",
        "help": "Manage vector index nodes (upload, delete, get)",
        "subcommands": {
            "upload": {
                "help": "Chunk and upload files as nodes",
                "args": [
                    {
                        "name": "--root",
                        "type": str,
                        "default": "./documentation",
                        "help": "Root directory containing markdown documentation.",
                    },
                    {
                        "name": "--index-id",
                        "type": str,
                        "default": "partner-gpt-index",
                        "help": "ID for the vector index to create/use.",
                    },
                    {
                        "name": "--dry-run",
                        "action": "store_true",
                        "help": "If set, only print chunk info and do not upload.",
                    },
                    {
                        "name": "--no-create-index",
                        "action": "store_true",
                        "help": "If set, do not create the index, just upload nodes.",
                    },
                    {
                        "name": "--chunk-size",
                        "type": int,
                        "default": DEFAULT_CHUNK_SIZE,
                        "help": "Maximum characters per chunk.",
                    },
                    {
                        "name": "--overlap",
                        "type": int,
                        "default": DEFAULT_CHUNK_OVERLAP,
                        "help": "Number of overlapping characters between chunks.",
                    },
                    {
                        "name": "--group-id",
                        "type": str,
                        "default": None,
                        "help": "Group ID for the nodes being uploaded.",
                    },
                ],
            },
            "delete-all": {
                "help": "Delete all nodes in the index",
                "args": [
                    {"name": "--index-id", "required": True, "help": "Index ID"},
                ],
            },
            "delete-by-id": {
                "help": "Delete nodes by nodeId",
                "args": [
                    {"name": "--index-id", "required": True, "help": "Index ID"},
                    {
                        "name": "--node-ids",
                        "nargs": "+",
                        "required": True,
                        "help": "List of nodeIds to delete",
                    },
                ],
            },
            "delete-by-group": {
                "help": "Delete nodes by nodeGroupId (groupId)",
                "args": [
                    {"name": "--index-id", "required": True, "help": "Index ID"},
                    {
                        "name": "--group-ids",
                        "nargs": "+",
                        "required": True,
                        "help": "List of groupIds to delete",
                    },
                ],
            },
            "get-all": {
                "help": "Fetch all node IDs from the specified index",
                "args": [
                    {"name": "--index-id", "required": True, "help": "Index ID"},
                ],
            },
        },
    },
}

ENDPOINTS = {
    "get_index": f"{API_URL_BASE}/recall/v1/indexes/{{index_id}}/get",
    "delete_index": f"{API_URL_BASE}/recall/v1/indexes/{{index_id}}/delete",
    "create_index": f"{API_URL_BASE}/recall/v1/indexes",
    "upsert_nodes": f"{API_URL_BASE}/recall/v1/indexes/{{index_id}}/upsert",
    "create_fileset": f"{API_URL_BASE}/files/v1/filesets/",
    "upload_file": f"{API_URL_BASE}/files/v1/filesets/{{fileset_id}}/files",
    "get_file": f"{API_URL_BASE}/files/v1/filesets/{{fileset_id}}/path",
    "get_file_by_id": f"{API_URL_BASE}/files/v1/filesets/{{fileset_id}}/files/{{file_id}}",
    "get_file_by_id_download": f"{API_URL_BASE}/files/v1/filesets/{{fileset_id}}/files/{{file_id}}/download",
}
