import os
from enum import Enum
from typing import Dict, Tuple
from dotenv import load_dotenv


# Enums for type-safe endpoint mapping
class IndexType(Enum):
    ENVIRONMENT = "environment"
    GLOBAL = "global"


class VectorOperation(Enum):
    CREATE_INDEX = "create_index"
    UPSERT_NODES = "upsert_nodes"
    GET_INDEX = "get_index"
    DELETE_INDEX = "delete_index"


load_dotenv()
API_URL_BASE = os.environ.get("DOMO_API_URL_BASE")
DEFAULT_CHUNK_SIZE = 1500
DEFAULT_CHUNK_OVERLAP = 200
DEFAULT_INDEX_ID = os.environ.get("VECTOR_INDEX_ID")

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
                        "default": DEFAULT_INDEX_ID,
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
                    {
                        "name": "--global",
                        "action": "store_true",
                        "help": "Use global vector index endpoints instead of environment-specific ones.",
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
    "create_index_global": f"{API_URL_BASE}/recall/v1/global/indexes",
    "upsert_nodes_global": f"{API_URL_BASE}/recall/v1/global/indexes/{{index_id}}/upsert",
    "create_fileset": f"{API_URL_BASE}/files/v1/filesets/",
    "upload_file": f"{API_URL_BASE}/files/v1/filesets/{{fileset_id}}/files",
    "get_file": f"{API_URL_BASE}/files/v1/filesets/{{fileset_id}}/path",
    "get_file_by_id": f"{API_URL_BASE}/files/v1/filesets/{{fileset_id}}/files/{{file_id}}",
    "get_file_by_id_download": f"{API_URL_BASE}/files/v1/filesets/{{fileset_id}}/files/{{file_id}}/download",
}

# Type-safe endpoint mapping
ENDPOINT_MAPPING: Dict[Tuple[IndexType, VectorOperation], str] = {
    (IndexType.ENVIRONMENT, VectorOperation.CREATE_INDEX): "create_index",
    (IndexType.GLOBAL, VectorOperation.CREATE_INDEX): "create_index_global",
    (IndexType.ENVIRONMENT, VectorOperation.UPSERT_NODES): "upsert_nodes",
    (IndexType.GLOBAL, VectorOperation.UPSERT_NODES): "upsert_nodes_global",
    (IndexType.ENVIRONMENT, VectorOperation.GET_INDEX): "get_index",
    (IndexType.ENVIRONMENT, VectorOperation.DELETE_INDEX): "delete_index",
}


def get_endpoint_key(operation: VectorOperation, is_global: bool = False) -> str:
    """
    Get the appropriate endpoint key for a vector operation.

    Args:
        operation: The vector operation to perform
        is_global: Whether to use global or environment-specific endpoints

    Returns:
        The endpoint key for use with ENDPOINTS dict

    Raises:
        KeyError: If the operation/index type combination is not supported
    """
    index_type = IndexType.GLOBAL if is_global else IndexType.ENVIRONMENT
    endpoint_key = ENDPOINT_MAPPING.get((index_type, operation))

    if endpoint_key is None:
        supported_ops = [
            op.value for op in VectorOperation if (index_type, op) in ENDPOINT_MAPPING
        ]
        raise KeyError(
            f"Unsupported operation '{operation.value}' for {index_type.value} index. "
            f"Supported operations: {supported_ops}"
        )

    return endpoint_key
