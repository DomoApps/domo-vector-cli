import os
import logging
from typing import Dict, Generator, List, Optional, Any, Tuple

from domo_vector_cli.constants import (
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_CHUNK_SIZE,
    VectorOperation,
    get_endpoint_key,
    get_endpoints,
)
from domo_vector_cli.config import config

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


async def handle_upload_cli(args: Any) -> None:
    """
    Handles the 'upload-nodes' command for the CLI.

    Processes supported document files (markdown, HTML, JSON, text) in the specified directory,
    chunks them into smaller pieces, and uploads to a vector index.

    Args:
        args: Command line arguments containing root directory, index ID, chunk size, etc.
    """
    print(f"Processing markdown files in {args.root} with index ID {args.index_id}")

    chunk_size = args.chunk_size if args.chunk_size else DEFAULT_CHUNK_SIZE
    overlap = args.overlap if args.overlap else DEFAULT_CHUNK_OVERLAP
    # Process markdown documents and create chunks
    chunks = await process_documents(
        root_dir=args.root,
        index_id=args.index_id,
        max_length=chunk_size,
        overlap=overlap,
        dry_run=args.dry_run,
        no_create_index=args.no_create_index,
    )

    if args.dry_run:
        index_type = "environment-specific"
        print(
            f"Dry run: {len(chunks)} chunks would be created and uploaded to {index_type} index."
        )
        for chunk in chunks:
            group_id = (
                args.group_id if args.group_id else os.path.basename(chunk["file_path"])
            )
            print(
                f"Chunk: {chunk['text'][:50]}... (from {chunk['file_path']})...(group: {group_id})"
            )
    else:
        print(f"Uploading {len(chunks)} chunks to index {args.index_id}...")
        await upload_chunks_to_vector_index(chunks, args.index_id, args.group_id)
        print("Upload complete.")


def process_html_file(file_path: str) -> Optional[str]:
    """Process HTML file and extract text content."""
    try:
        text = read_file_contents(file_path)
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(text, "html.parser")
        extracted_text = soup.get_text(separator="\n")
        logger.debug(f"Successfully extracted text from HTML file {file_path}")
        return extracted_text
    except ImportError:
        logger.error(f"BeautifulSoup4 not available for HTML parsing: {file_path}")
        return None
    except Exception as e:
        logger.error(f"Failed to parse HTML file {file_path}: {e}")
        return None


def process_json_file(file_path: str) -> List[Dict[str, str]]:
    """Process JSON file and return chunks."""
    import json

    chunks = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            logger.warning(f"JSON file {file_path} does not contain a list, skipping")
            return chunks

        for i, json_chunk in enumerate(data):
            if not isinstance(json_chunk, dict) or "title" not in json_chunk:
                logger.warning(
                    f"JSON chunk {i} in {file_path} missing 'title' field, skipping"
                )
                continue

            try:
                chunk_text = json.dumps(
                    f"{json_chunk['title']}: {json_chunk}",
                    ensure_ascii=False,
                    indent=2,
                )
                chunk_file_path = json_chunk["title"]
                chunks.append({"text": chunk_text, "file_path": chunk_file_path})
            except (TypeError, KeyError) as e:
                logger.error(f"Error processing JSON chunk {i} in {file_path}: {e}")
                continue

        logger.info(
            f"Successfully processed {len(chunks)} JSON chunks from {file_path}"
        )
        return chunks

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in file {file_path}: {e}")
        return chunks
    except IOError as e:
        logger.error(f"Error reading JSON file {file_path}: {e}")
        return chunks
    except Exception as e:
        logger.error(f"Unexpected error parsing JSON file {file_path}: {e}")
        return chunks


def process_text_file(
    file_path: str, max_length: int, overlap: int
) -> List[Dict[str, str]]:
    """Process text-based file (markdown, txt) and return chunks."""
    try:
        text = read_file_contents(file_path)
        chunk_list = chunk_text_with_overlap(
            text, max_length=max_length, overlap=overlap
        )
        return [{"text": chunk, "file_path": file_path} for chunk in chunk_list]
    except Exception as e:
        logger.error(f"Error processing text file {file_path}: {e}")
        return []


async def process_documents(
    root_dir: str,
    index_id: str,
    max_length: int,
    overlap: int,
    dry_run: bool = False,
    no_create_index: bool = False,
) -> List[Dict[str, str]]:
    """
    Creates a vector index and processes all supported files in a directory.

    Processes markdown, HTML, JSON, and text files from the directory tree,
    splitting them into overlapping chunks for vector indexing.

    Args:
        root_dir: Root directory to scan for documents
        index_id: ID for the vector index to create/use
        max_length: Maximum characters per chunk
        overlap: Number of overlapping characters between chunks
        dry_run: If True, only simulate processing without creating index
        no_create_index: If True, skip index creation step

    Returns:
        List of chunk dictionaries containing text and file path metadata
    """
    # Create the index first
    if not dry_run and not no_create_index:
        index_type = "environment-specific"
        logger.info(f"Creating {index_type} vector index with ID: {index_id}")
        await create_vector_index(index_id)

    chunks = []
    processed_files = 0
    skipped_files = 0

    for file_path in iterate_documents_breadth_first(root_dir):
        ext = os.path.splitext(file_path)[1].lower()

        if ext in [".md", ".txt"]:
            file_chunks = process_text_file(file_path, max_length, overlap)
            chunks.extend(file_chunks)
            if file_chunks:
                processed_files += 1
            else:
                skipped_files += 1

        elif ext == ".html":
            text = process_html_file(file_path)
            if text:
                chunk_list = chunk_text_with_overlap(
                    text, max_length=max_length, overlap=overlap
                )
                file_chunks = [
                    {"text": chunk, "file_path": file_path} for chunk in chunk_list
                ]
                chunks.extend(file_chunks)
                processed_files += 1
            else:
                skipped_files += 1

        elif ext == ".json":
            json_chunks = process_json_file(file_path)
            chunks.extend(json_chunks)
            if json_chunks:
                processed_files += 1
            else:
                skipped_files += 1
        else:
            logger.debug(f"Skipping unsupported file type: {file_path}")
            skipped_files += 1
            continue

    logger.info(
        f"Processed {processed_files} files, skipped {skipped_files} files, generated {len(chunks)} chunks"
    )
    return chunks


async def create_vector_index(
    index_id: str,
    embedding_model: str = "domo.openai",
) -> Dict[str, Any]:
    """
    Creates a remote vector index via the Domo Recall API.

    Args:
        index_id: The ID for the vector index
        embedding_model: The embedding model to use (default: "domo.domo_ai.domo-embed-text-multilingual-v1:cohere")

    Returns the index info as a dict.
    """
    import httpx

    endpoints = get_endpoints()
    endpoint_key = get_endpoint_key(VectorOperation.CREATE_INDEX)
    url = endpoints[endpoint_key]
    payload = {"embeddingModel": embedding_model, "indexId": index_id}
    headers = config.get_headers()

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()


def chunk_text_with_overlap(text: str, max_length: int, overlap: int) -> List[str]:
    """
    Splits text into overlapping chunks, each less than max_length characters.
    Overlap ensures context is preserved between chunks.
    Uses LangChain's CharacterTextSplitter for robust chunking.
    """
    from langchain_text_splitters import CharacterTextSplitter

    print(
        f"Chunking text of length {len(text)} into max {max_length} characters with overlap {overlap}"
    )
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=max_length,
        chunk_overlap=overlap,
        length_function=len,
    )
    return splitter.split_text(text)


async def upload_chunks_to_vector_index(
    chunks: List[Dict[str, str]], index_id: str, group_id: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Uploads a list of chunk dictionaries to the specified vector index via the Domo Recall API.

    Args:
        chunks: List of chunk dictionaries containing text and metadata
        index_id: The ID of the vector index to upload to
        group_id: Optional group ID for the chunks

    Each chunk should contain the text and any relevant metadata.
    """
    import httpx
    import uuid

    endpoints = get_endpoints()
    endpoint_key = get_endpoint_key(VectorOperation.UPSERT_NODES)
    url = endpoints[endpoint_key].replace("{index_id}", index_id)
    headers = config.get_headers()

    index_type = "environment-specific"
    logger.info(f"Using {index_type} vector index endpoints")
    token_preview = (
        headers["x-domo-developer-token"][:8] + "..."
        if headers["x-domo-developer-token"]
        else "None"
    )
    logger.debug(f"developer token preview: {token_preview}")
    batch_size = 50
    total = len(chunks)
    results = []
    total_batches = (total + batch_size - 1) // batch_size
    async with httpx.AsyncClient() as client:
        for i in range(0, total, batch_size):
            batch = chunks[i : i + batch_size]
            nodes = []
            for chunk in batch:
                node_group_id = (
                    group_id if group_id else os.path.basename(chunk["file_path"])
                )
                content = chunk["text"]
                # Defensive: ensure content is a string
                if not isinstance(content, str):
                    logger.warning(
                        f"Node content for file {chunk.get('file_path', 'unknown')} is not a string (type={type(content)}). Attempting to convert."
                    )
                    if isinstance(content, dict):
                        import json

                        content = json.dumps(content, ensure_ascii=False)
                    else:
                        content = str(content)
                node = {
                    "id": str(uuid.uuid4()),
                    "content": content,
                    "type": "TEXT",
                    "groupId": node_group_id,
                }
                # Optional: validate node structure
                if not all(k in node for k in ("id", "content", "type", "groupId")):
                    logger.error(f"Node missing required keys: {node}")
                    continue
                nodes.append(node)
            payload = {"nodes": nodes}
            # Log only the first node in the batch for debugging
            if nodes:
                logger.info(
                    f"First node in batch {i//batch_size+1}/{total_batches}: (file: {batch[0].get('file_path', 'unknown')}) {nodes[0]}"
                )
            try:
                logger.info(
                    f"Uploading batch {i//batch_size+1}/{total_batches} ({len(nodes)} nodes) to index {index_id}..."
                )
                response = await client.post(
                    url, json=payload, headers=headers, timeout=60
                )
                response.raise_for_status()
                logger.info(
                    f"Batch {i//batch_size+1}/{total_batches} uploaded successfully."
                )
                results.append(response.json())
            except httpx.HTTPStatusError as e:
                logger.error(
                    f"HTTP error uploading batch {i//batch_size+1}/{total_batches}: {e.response.status_code} - {e.response.text}"
                )
            except Exception as e:
                logger.error(
                    f"Unexpected error uploading batch {i//batch_size+1}/{total_batches}: {e}"
                )
    return results


def read_file_contents(file_path: str) -> str:
    """
    Reads and returns the contents of a file at the given path.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def iterate_documents_breadth_first(root_dir: str) -> Generator[str, None, None]:
    """
    Yields file paths in the documentation directory using breadth-first traversal.
    """
    import os
    from collections import deque

    queue = deque([root_dir])
    while queue:
        current_dir = queue.popleft()
        with os.scandir(current_dir) as it:
            for entry in it:
                if entry.is_dir():
                    queue.append(entry.path)
                elif entry.is_file():
                    yield entry.path
