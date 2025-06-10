import os
from dotenv import load_dotenv

load_dotenv()
API_URL_BASE = os.environ.get("DOMO_API_URL_BASE", "https://domo-es.domo.com/api")
DEFAULT_CHUNK_SIZE = 1500
DEFAULT_CHUNK_OVERLAP = 200

COMMANDS = {
    "upload_nodes": {
        "name": "upload-nodes",
        "help": "Chunk and upload files",
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
    "delete_all": {
        "name": "delete-all",
        "help": "Delete all nodes in the index",
        "args": [
            {"name": "--index-id", "required": True, "help": "Index ID"},
        ],
    },
    "delete_by_id": {
        "name": "delete-by-id",
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
    "delete_by_group": {
        "name": "delete-by-group",
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
    "get_all": {
        "name": "get-all",
        "help": "Fetch all node IDs from the specified index",
        "args": [
            {"name": "--index-id", "required": True, "help": "Index ID"},
        ],
    },
    "configure": {
        "name": "configure",
        "help": "Configure the CLI with environment variables",
    },
    "help": {
        "name": "help",
        "help": "Show this help message and exit",
    },
}

ENDPOINTS = {
    "get_index": f"{API_URL_BASE}/recall/v1/indexes/{{index_id}}/get",
    "delete_index": f"{API_URL_BASE}/recall/v1/indexes/{{index_id}}/delete",
    "create_index": f"{API_URL_BASE}/recall/v1/indexes",
    "upsert_nodes": f"{API_URL_BASE}/recall/v1/indexes/{{index_id}}/upsert",
}
