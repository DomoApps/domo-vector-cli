import os
from typing import Dict, Generator, List

from constants import API_URL_BASE, DEFAULT_CHUNK_OVERLAP, DEFAULT_CHUNK_SIZE


async def handle_upload_cli(args):
    """
    Handles the 'upload-nodes' command for the CLI, processing markdown files in the specified directory,
    chunking them, and uploading to the vector index.
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
    )

    if args.dry_run:
        print(f"Dry run: {len(chunks)} chunks would be created.")
        for chunk in chunks:
            print(f"Chunk: {chunk['text'][:50]}... (from {chunk['file_path']})")
    else:
        print(f"Uploading {len(chunks)} chunks to index {args.index_id}...")
        await upload_chunks_to_vector_index(chunks, args.index_id)
        print("Upload complete.")


async def process_documents(
    root_dir: str,
    index_id: str,
    max_length: int,
    overlap: int,
    dry_run: bool = False,
) -> List[Dict]:
    """
    Creates the index, then iterates through all markdown files in the directory, reads their contents,
    and splits them into overlapping chunks using LangChain's CharacterTextSplitter.
    Returns a list of dicts with chunk text and metadata.
    """
    # Create the index first
    if not dry_run:
        print(f"Creating vector index with ID: {index_id}")
        await create_vector_index(index_id)

    chunks = []
    for file_path in iterate_documents_breadth_first(root_dir):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".md":
            text = read_file_contents(file_path)
            # Optionally, preprocess markdown (e.g., strip frontmatter)
        elif ext == ".html":
            text = read_file_contents(file_path)
            # Optionally, extract visible text from HTML
            try:
                from bs4 import BeautifulSoup

                soup = BeautifulSoup(text, "html.parser")
                text = soup.get_text(separator="\n")
            except ImportError:
                print("BeautifulSoup4 is not installed. HTML files will not be parsed.")
        elif ext == ".json":
            import json

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                # Convert JSON to a string representation for chunking
                import pprint

                text = pprint.pformat(data)
            except Exception as e:
                print(f"Failed to parse JSON file {file_path}: {e}")
                continue
        else:
            # Skip unsupported file types
            continue

        chunk_list = chunk_text_with_overlap(
            text, max_length=max_length, overlap=overlap
        )
        for i, chunk in enumerate(chunk_list):
            chunks.append({"text": chunk, "file_path": file_path, "chunk_index": i})
    return chunks


async def create_vector_index(
    index_id: str, embedding_model: str = "domo.openai"
) -> dict:
    """
    Creates a remote vector index via the Domo Recall API.
    Returns the index info as a dict.
    """
    import httpx

    from constants import ENDPOINTS

    url = ENDPOINTS["create_index"]
    payload = {"embeddingModel": embedding_model, "indexId": index_id}
    headers = {"x-domo-developer-token": os.environ.get("DOMO_DEVELOPER_TOKEN", "")}
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
    from langchain.text_splitter import CharacterTextSplitter

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


async def upload_chunks_to_vector_index(chunks: List[Dict], index_id: str):
    """
    Uploads a list of chunk dictionaries to the specified vector index via the Domo Recall API.
    Each chunk should contain the text and any relevant metadata.
    """
    import httpx, uuid, os

    from constants import ENDPOINTS

    url = ENDPOINTS["upsert_index"].replace("{index_id}", index_id)

    nodes = []
    for chunk in chunks:
        # Extract the file name from the file_path for groupId
        file_name = os.path.basename(chunk["file_path"])
        node = {
            "id": str(uuid.uuid4()),
            "content": chunk["text"],
            "type": "TEXT",
            "groupId": file_name,
        }
        nodes.append(node)

    payload = {"nodes": nodes}
    headers = {"x-domo-developer-token": os.environ.get("DOMO_DEVELOPER_TOKEN", "")}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()


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
