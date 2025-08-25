"""
Handler functions for fileset-related CLI commands: create, upload-file, get-file, get-fileset, get-filesets.
"""

import os
import requests
from domo_vector_cli.constants import get_endpoints


def create_fileset(
    name,
    description=None,
    account_id=None,
    ai_enabled=True,
    batch_type="INCREMENTAL",
    connector="DOMO",
):
    endpoints = get_endpoints()
    url = endpoints["create_fileset"]
    token = os.environ.get("DOMO_DEVELOPER_TOKEN")
    if not token:
        raise RuntimeError("DOMO_DEVELOPER_TOKEN environment variable not set.")
    headers = {
        "Content-Type": "application/json",
        "x-domo-developer-token": token,
    }
    body = {
        "accountId": account_id,
        "aiEnabled": ai_enabled,
        "batchType": batch_type,
        "connector": connector,
        "description": description,
        "name": name,
    }
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    return response.json()


def upload_file_to_fileset(fileset_id, file_path, directory_path):
    """
    Upload a file to a fileset using multipart/form-data.
    """
    import logging
    import mimetypes
    import json

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Register YAML MIME types for .yaml and .yml
    mimetypes.add_type("application/x-yaml", ".yaml")
    mimetypes.add_type("application/x-yaml", ".yml")

    token = os.environ.get("DOMO_DEVELOPER_TOKEN")
    if not token:
        logger.error("DOMO_DEVELOPER_TOKEN environment variable not set.")
        raise RuntimeError("DOMO_DEVELOPER_TOKEN environment variable not set.")
    endpoints = get_endpoints()
    url = endpoints["upload_file"].format(fileset_id=fileset_id)
    headers = {
        "x-domo-developer-token": token,
    }
    logger.info(
        f"Uploading file: {file_path} to fileset: {fileset_id} at directory: '{directory_path}'"
    )
    try:
        # Skip upload if file is empty
        if os.path.getsize(file_path) == 0:
            logger.info(f"Skipping empty file: {file_path}")
            return {"skipped": True, "reason": "empty file", "file": file_path}

        content_type = "text/plain"
        logger.info(f"Determined content type: {content_type}")
        with open(file_path, "rb") as f:
            files = {
                "file": (os.path.basename(file_path), f, content_type),
                "createFileRequest": (
                    None,
                    f'{{"directoryPath":"{directory_path}"}}',
                    "application/json",
                ),
            }
            logger.debug(
                f"Files dict (no file content): {{'file': (name: {os.path.basename(file_path)}, content_type: {content_type}), 'createFileRequest': (json)}}"
            )
            response = requests.post(url, headers=headers, files=files)
        logger.info(f"Response status code: {response.status_code}")
        if not response.ok:
            logger.error(
                f"Error uploading file: {response.status_code} {response.text}"
            )
            # Log failure to a file for retry
            fail_log = {
                "file_path": file_path,
                "directory_path": directory_path,
                "fileset_id": fileset_id,
                "status_code": response.status_code,
                "response_text": response.text,
            }
            with open("failed_uploads.log", "a") as flog:
                flog.write(json.dumps(fail_log) + "\n")
            return {"failed": True, "reason": response.text, "file": file_path}
        return response.json()
    except Exception as e:
        logger.exception(f"Exception occurred while uploading file: {file_path}")
        # Log exception to a file for retry
        fail_log = {
            "file_path": file_path,
            "directory_path": directory_path,
            "fileset_id": fileset_id,
            "exception": str(e),
        }
        with open("failed_uploads.log", "a") as flog:
            flog.write(json.dumps(fail_log) + "\n")
        return {"failed": True, "reason": str(e), "file": file_path}


def upload_directory_to_fileset(fileset_id, root_dir):
    """
    Walk the directory breadth-first and upload all files, preserving relative paths.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Sort dirnames and filenames for deterministic order (breadth-first)
        dirnames.sort()
        filenames.sort()
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            rel_dir = os.path.relpath(dirpath, root_dir)
            # If rel_dir is '.', treat as root
            directory_path = rel_dir if rel_dir != "." else ""
            print(
                f"Uploading {file_path} to fileset {fileset_id} at directory '{directory_path}'..."
            )
            upload_file_to_fileset(fileset_id, file_path, directory_path)


def get_file_from_fileset(fileset_id, file_path=None, file_id=None, output_path=None):
    """
    Download a file from a fileset using either the path or fileId endpoint.
    If file_path is provided, query for the file object, extract fileId, and download.
    If file_id is provided, download directly.
    """
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    import json

    token = os.environ.get("DOMO_DEVELOPER_TOKEN")
    if not token:
        logger.error("DOMO_DEVELOPER_TOKEN environment variable not set.")
        raise RuntimeError("DOMO_DEVELOPER_TOKEN environment variable not set.")
    headers = {"x-domo-developer-token": token}

    def download_by_id(fileset_id, file_id, out_name):
        endpoints = get_endpoints()
        url = endpoints["get_file_by_id_download"].format(
            fileset_id=fileset_id, file_id=file_id
        )
        resp = requests.get(url, headers=headers, stream=True)
        if resp.status_code == 200:
            with open(out_name, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            logger.info(f"File downloaded to {out_name}")
            return {"success": True, "output_path": out_name}
        else:
            logger.error(f"Failed to download file: {resp.status_code} {resp.text}")
            return {
                "success": False,
                "status_code": resp.status_code,
                "error": resp.text,
            }

    if file_path:
        # Query file object by path
        endpoints = get_endpoints()
        url = endpoints["get_file"].format(fileset_id=fileset_id)
        params = {"path": file_path}
        logger.info(
            f"Querying file object by path: {file_path} from fileset: {fileset_id}"
        )
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code == 200:
            file_obj = resp.json()
            file_id = file_obj.get("id")
            out_name = (
                output_path or file_obj.get("name") or os.path.basename(file_path)
            )
            if file_id:
                return download_by_id(fileset_id, file_id, out_name)
            else:
                logger.error(f"No file id found in file object: {json.dumps(file_obj)}")
                return {
                    "success": False,
                    "error": "No file id in file object",
                    "file_obj": file_obj,
                }
        else:
            logger.error(f"Failed to query file object: {resp.status_code} {resp.text}")
            return {
                "success": False,
                "status_code": resp.status_code,
                "error": resp.text,
            }
    elif file_id:
        out_name = output_path or f"{file_id}"
        return download_by_id(fileset_id, file_id, out_name)
    else:
        logger.error("You must provide either file_path or file_id.")
        return {"success": False, "error": "No file_path or file_id provided."}


def get_file_text_from_fileset(fileset_id, file_path=None, file_id=None):
    """
    Retrieve the text content of a file from a fileset (no download, just return text).
    If file_path is provided, query for the file object, extract fileId, and fetch text.
    If file_id is provided, fetch text directly.
    """
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    import json

    token = os.environ.get("DOMO_DEVELOPER_TOKEN")
    if not token:
        logger.error("DOMO_DEVELOPER_TOKEN environment variable not set.")
        raise RuntimeError("DOMO_DEVELOPER_TOKEN environment variable not set.")
    headers = {"x-domo-developer-token": token}

    def fetch_text_by_id(fileset_id, file_id):
        endpoints = get_endpoints()
        url = endpoints["get_file_by_id_download"].format(
            fileset_id=fileset_id, file_id=file_id
        )
        resp = requests.get(url, headers=headers, stream=True)
        if resp.status_code == 200:
            # Try to decode as text
            try:
                text = resp.content.decode("utf-8")
                logger.info(f"File text retrieved successfully for file_id: {file_id}")
                logger.info(f"File text length: {len(text)} characters")
                return {"success": True, "text": resp.content.decode("utf-8")}
            except Exception as e:
                logger.error(f"Failed to decode file as text: {e}")
                return {"success": False, "error": str(e)}
        else:
            logger.error(f"Failed to fetch file: {resp.status_code} {resp.text}")
            return {
                "success": False,
                "status_code": resp.status_code,
                "error": resp.text,
            }

    if file_path:
        # Query file object by path
        endpoints = get_endpoints()
        url = endpoints["get_file"].format(fileset_id=fileset_id)
        params = {"path": file_path}
        logger.info(
            f"Querying file object by path: {file_path} from fileset: {fileset_id}"
        )
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code == 200:
            file_obj = resp.json()
            file_id = file_obj.get("id")
            if file_id:
                return fetch_text_by_id(fileset_id, file_id)
            else:
                logger.error(f"No file id found in file object: {json.dumps(file_obj)}")
                return {
                    "success": False,
                    "error": "No file id in file object",
                    "file_obj": file_obj,
                }
        else:
            logger.error(f"Failed to query file object: {resp.status_code} {resp.text}")
            return {
                "success": False,
                "status_code": resp.status_code,
                "error": resp.text,
            }
    elif file_id:
        return fetch_text_by_id(fileset_id, file_id)
    else:
        logger.error("You must provide either file_path or file_id.")
        return {"success": False, "error": "No file_path or file_id provided."}


def get_all_filesets():
    """
    Get all filesets using GET /api/files/v1/filesets.
    Returns the list of all filesets.
    """
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    token = os.environ.get("DOMO_DEVELOPER_TOKEN")
    if not token:
        logger.error("DOMO_DEVELOPER_TOKEN environment variable not set.")
        raise RuntimeError("DOMO_DEVELOPER_TOKEN environment variable not set.")
    headers = {"x-domo-developer-token": token}
    
    endpoints = get_endpoints()
    url = endpoints["search_filesets"]
    
    logger.info("Fetching all filesets...")
    # Use POST with proper payload structure
    headers["Content-Type"] = "application/json"
    payload = {
        "fieldSort": [{"field": "updated", "order": "DESC"}],
        "filters": [{"field": "name", "value": [""], "not": False, "operator": "LIKE"}],
        "dateFilters": []
    }
    resp = requests.post(url, headers=headers, json=payload)
    if resp.status_code == 200:
        response_data = resp.json()
        filesets = response_data.get("fileSets", [])
        logger.info(f"Found {len(filesets)} filesets.")
        return {"success": True, "filesets": filesets}
    else:
        logger.error(f"Failed to get filesets: {resp.status_code} {resp.text}")
        return {"success": False, "status_code": resp.status_code, "error": resp.text}


def get_fileset_metadata(fileset_id):
    """
    Get metadata for a specific fileset using GET /api/files/v1/filesets/{fileset_id}.
    Returns the fileset metadata.
    """
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    token = os.environ.get("DOMO_DEVELOPER_TOKEN")
    if not token:
        logger.error("DOMO_DEVELOPER_TOKEN environment variable not set.")
        raise RuntimeError("DOMO_DEVELOPER_TOKEN environment variable not set.")
    headers = {"x-domo-developer-token": token}
    
    endpoints = get_endpoints()
    url = endpoints["get_fileset"].format(fileset_id=fileset_id)
    
    logger.info(f"Fetching metadata for fileset {fileset_id}...")
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        fileset = resp.json()
        logger.info(f"Found fileset: {fileset.get('name', fileset.get('id'))}")
        return {"success": True, "fileset": fileset}
    else:
        logger.error(f"Failed to get fileset metadata: {resp.status_code} {resp.text}")
        return {"success": False, "status_code": resp.status_code, "error": resp.text}


def search_filesets(
    limit=10, offset=0, field_sort=None, filters=None, date_filters=None
):
    """
    Search for filesets using POST /api/files/v1/filesets/search.
    Returns the list of filesets matching the criteria.
    """
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    import json

    token = os.environ.get("DOMO_DEVELOPER_TOKEN")
    if not token:
        logger.error("DOMO_DEVELOPER_TOKEN environment variable not set.")
        raise RuntimeError("DOMO_DEVELOPER_TOKEN environment variable not set.")
    headers = {
        "x-domo-developer-token": token,
        "Content-Type": "application/json",
    }
    endpoints = get_endpoints()
    url = f"{endpoints['search_filesets']}?limit={limit}&offset={offset}"
    body = {
        "fieldSort": (
            field_sort
            if field_sort is not None
            else [{"field": "updated", "order": "DESC"}]
        ),
        "filters": filters if filters is not None else [],
        "dateFilters": date_filters if date_filters is not None else [],
    }
    logger.info(f"Searching filesets with body: {json.dumps(body)}")
    resp = requests.post(url, headers=headers, json=body)
    if resp.status_code == 200:
        response_data = resp.json()
        filesets = response_data.get("fileSets", [])
        logger.info(f"Found {len(filesets)} filesets.")
        return {"success": True, "filesets": filesets}
    else:
        logger.error(f"Failed to search filesets: {resp.status_code} {resp.text}")
        return {"success": False, "status_code": resp.status_code, "error": resp.text}


async def handle_fileset_cli(args):
    if args.fileset_command == "create":
        result = create_fileset(name=args.name, description=args.description)
        print("Fileset created:", result)
    elif args.fileset_command == "upload-file":
        # If a directory is provided, check if it's a file or directory
        if hasattr(args, "directory") and args.directory:
            if os.path.isfile(args.directory):
                # Upload as a single file, directory_path is ''
                print(
                    f"Uploading file {args.directory} to fileset {args.fileset_id}..."
                )
                result = upload_file_to_fileset(args.fileset_id, args.directory, "")
                print("File uploaded:", result)
            elif os.path.isdir(args.directory):
                upload_directory_to_fileset(args.fileset_id, args.directory)
            else:
                print(f"Path {args.directory} does not exist.")
        else:
            print(f"Uploading file {args.file_path} to fileset {args.fileset_id}...")
            directory_path = getattr(args, "directory_path", "") or ""
            result = upload_file_to_fileset(
                args.fileset_id, args.file_path, directory_path
            )
            print("File uploaded:", result)
    elif args.fileset_command == "get-file":
        print(f"Getting file {args.file_id} from fileset {args.fileset_id}...")
        if not args.file_path and not args.file_id:
            print("You must provide either a file path or a file ID to get a file.")
            return
        if args.file_path:
            print(
                f"Fetching file at path {args.file_path} from fileset {args.fileset_id}..."
            )
            # If file_path is provided, we can directly get the file
            get_file_text_from_fileset(args.fileset_id, args.file_path, None)
        elif args.file_id:
            print(
                f"Fetching file with ID {args.file_id} from fileset {args.fileset_id}..."
            )
            get_file_text_from_fileset(args.fileset_id, None, args.file_id)
    elif args.fileset_command == "get-fileset":
        print(f"Getting fileset {args.fileset_id}...")
        result = get_fileset_metadata(args.fileset_id)
        if result["success"]:
            fileset = result["fileset"]
            print(f"Fileset: {fileset.get('name', 'Unknown')} (ID: {fileset.get('id')})")
            print(f"Description: {fileset.get('description', 'No description')}")
            print(f"Created: {fileset.get('createdAt', 'Unknown')}")
            print(f"Updated: {fileset.get('updatedAt', 'Unknown')}")
            print(f"File count: {fileset.get('fileCount', 0)}")
        else:
            print(f"Error getting fileset: {result.get('error')}")
    elif args.fileset_command == "get-filesets":
        print("Listing all filesets...")
        result = get_all_filesets()
        if result["success"]:
            print(f"Found {len(result['filesets'])} filesets:")
            for fs in result["filesets"]:
                print(
                    f"- {fs.get('name', fs.get('id', 'unknown'))} (ID: {fs.get('id')})"
                )
        else:
            print(f"Error listing filesets: {result.get('error')}")
    elif args.fileset_command == "search-filesets":
        # Handle search-filesets CLI command
        limit = getattr(args, "limit", 10)
        offset = getattr(args, "offset", 0)
        name_filter = getattr(args, "name", None)
        
        filters = None
        if name_filter:
            filters = [{"field": "name", "value": [name_filter], "not": False, "operator": "LIKE"}]
        
        result = search_filesets(limit=limit, offset=offset, filters=filters)
        if result["success"]:
            print(f"Found {len(result['filesets'])} filesets:")
            for fs in result["filesets"]:
                print(
                    f"- {fs.get('name', fs.get('id', 'unknown'))} (ID: {fs.get('id')})"
                )
        else:
            print(f"Error searching filesets: {result.get('error')}")
    else:
        print("Unknown fileset command.")
