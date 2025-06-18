"""
Handler functions for fileset-related CLI commands: create, upload-file, get-file, get-fileset, get-filesets.
"""

import os
import requests
from domo_vector_cli.constants import ENDPOINTS


def create_fileset(
    name,
    description=None,
    account_id=None,
    ai_enabled=True,
    batch_type="INCREMENTAL",
    connector="DOMO",
):
    url = ENDPOINTS["create_fileset"]
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
    url = ENDPOINTS["upload_file"].format(fileset_id=fileset_id)
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


def handle_fileset_cli(args):
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
        # Implement get file logic here
    elif args.fileset_command == "get-fileset":
        print(f"Getting fileset {args.fileset_id}...")
        # Implement get fileset logic here
    elif args.fileset_command == "get-filesets":
        print("Listing all filesets...")
        # Implement list filesets logic here
    else:
        print("Unknown fileset command.")
