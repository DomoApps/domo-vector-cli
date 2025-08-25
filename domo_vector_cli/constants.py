import os
from enum import Enum
from typing import Dict, Tuple


# Enums for type-safe endpoint mapping
class IndexType(Enum):
    ENVIRONMENT = "environment"


class VectorOperation(Enum):
    CREATE_INDEX = "create_index"
    UPSERT_NODES = "upsert_nodes"
    GET_INDEX = "get_index"
    DELETE_INDEX = "delete_index"


# These are imported from config now, but kept here for backward compatibility
DEFAULT_CHUNK_SIZE = 1500
DEFAULT_CHUNK_OVERLAP = 200


# Dynamic API URL base - will be loaded from config when accessed
def get_api_url_base() -> str:
    """Get API URL base from configuration."""
    from domo_vector_cli.config import config

    return config.domo.api_url_base


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
                "help": "Create a new Fileset",
                "args": [
                    {"name": "--name", "required": True, "help": "Name of the fileset"},
                    {
                        "name": "--description",
                        "required": False,
                        "help": "Description of the Fileset",
                    },
                ],
            },
            "upload-file": {
                "help": "Upload a file or directory to a Fileset",
                "args": [
                    {
                        "name": "--fileset-id",
                        "required": True,
                        "help": "ID of the Fileset",
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
                "help": "Get a file from a Fileset",
                "args": [
                    {
                        "name": "--fileset-id",
                        "required": True,
                        "help": "ID of the Fileset",
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
                "help": "Get a Fileset by ID",
                "args": [
                    {
                        "name": "--fileset-id",
                        "required": True,
                        "help": "ID of the Fileset",
                    }
                ],
            },
            "get-filesets": {"help": "List all Fileset", "args": []},
            "search-filesets": {
                "help": "List/Search Fileset (with optional sort, filters, pagination)",
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
                    {
                        "name": "--name",
                        "type": str,
                        "required": False,
                        "help": "Search filesets by name (partial matching supported)",
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
                        "name": "--source-dir",
                        "type": str,
                        "required": True,
                        "help": "Source directory containing files to process.",
                    },
                    {
                        "name": "--index-id",
                        "type": str,
                        "default": None,
                        "help": "ID for the vector index to create/use (uses VECTOR_INDEX_ID from .env if not specified).",
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
                        "name": "--include-images",
                        "action": "store_true",
                        "help": "If set, also process and embed image files (png, jpg, jpeg, gif, bmp, webp, tiff).",
                    },
                ],
            },
            "delete-all": {
                "help": "Delete ALL nodes in the index",
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


def get_endpoints() -> Dict[str, str]:
    """Get API endpoints with dynamic base URL."""
    api_base = get_api_url_base()
    return {
        "get_index": f"{api_base}/recall/v1/indexes/{{index_id}}/get",
        "delete_index": f"{api_base}/recall/v1/indexes/{{index_id}}/delete",
        "create_index": f"{api_base}/recall/v1/indexes",
        "upsert_nodes": f"{api_base}/recall/v1/indexes/{{index_id}}/upsert",
        "image_embedding": f"{api_base}/ai/v1/embedding/image",
        "create_fileset": f"{api_base}/files/v1/filesets",
        "get_filesets": f"{api_base}/files/v1/filesets",
        "get_fileset": f"{api_base}/files/v1/filesets/{{fileset_id}}",
        "search_filesets": f"{api_base}/files/v1/filesets/search",
        "upload_file": f"{api_base}/files/v1/filesets/{{fileset_id}}/files",
        "get_file": f"{api_base}/files/v1/filesets/{{fileset_id}}/path",
        "get_file_by_id": f"{api_base}/files/v1/filesets/{{fileset_id}}/files/{{file_id}}",
        "get_file_by_id_download": f"{api_base}/files/v1/filesets/{{fileset_id}}/files/{{file_id}}/download",
    }


# Backward compatibility - this will be deprecated
ENDPOINTS = {}

# Type-safe endpoint mapping
ENDPOINT_MAPPING: Dict[Tuple[IndexType, VectorOperation], str] = {
    (IndexType.ENVIRONMENT, VectorOperation.CREATE_INDEX): "create_index",
    (IndexType.ENVIRONMENT, VectorOperation.UPSERT_NODES): "upsert_nodes",
    (IndexType.ENVIRONMENT, VectorOperation.GET_INDEX): "get_index",
    (IndexType.ENVIRONMENT, VectorOperation.DELETE_INDEX): "delete_index",
}


def get_endpoint_key(operation: VectorOperation) -> str:
    """
    Get the appropriate endpoint key for a vector operation.

    Args:
        operation: The vector operation to perform

    Returns:
        The endpoint key for use with ENDPOINTS dict

    Raises:
        KeyError: If the operation/index type combination is not supported
    """
    index_type = IndexType.ENVIRONMENT
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
