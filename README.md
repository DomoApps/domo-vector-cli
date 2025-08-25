# Domo Vector CLI Tool

A Python CLI tool for chunking, uploading, and managing documentation files (Markdown, HTML, JSON, PDF) and images in a Domo vector index or fileset. Supports robust batching, error handling, retry logging, and configuration via `.env`.

---

## Features

### Vector Index Management

- Chunk and upload Markdown, HTML, JSON, and PDF files to a Domo vector index
- Process and embed image files (PNG, JPG, JPEG, GIF, BMP, WebP, TIFF) for vector search
- Robust batch uploads with error handling and retry logging (failed uploads are logged for retry)
- Delete nodes from a vector index:
  - By node ID (`vector delete-by-id`)
  - By group ID (`vector delete-by-group`)
  - Delete all nodes without a group (`vector delete-all`)
- Fetch all node IDs from an index (`vector get-all`)
- Configure your Domo API key and instance URL interactively

### Fileset Management

- Create new FileSets
- Upload files or entire directories to FileSets
- Download files from FileSets
- Get FileSet metadata and list files
- Search FileSets by name or metadata
- Fetch file text content directly (without saving to disk)

---

## Prerequisites

### System Requirements

- **Python 3.8 or higher** - Check with `python --version` or `python3 --version`
- **pip** - Python package installer (usually comes with Python)
- **Git** - For cloning the repository

### Domo Requirements

- **Domo Instance Access** - You need access to a Domo instance (e.g., `your-company.domo.com`)
- **Developer Token** - A Domo Developer API token with appropriate permissions
  - Log into your Domo instance
  - Go to Admin > Authentication > Access Tokens
  - Create a new Developer Token and make sure you save it somewhere safe for reference

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:DomoApps/domo-vector-cli.git
   cd domo-vector-cli
   ```

2. **Install dependencies and the CLI tool locally:**
   ```bash
   pip install -e .
   ```
   This will make the `domo-vector` command available globally.

---

## Configuration

Before using the CLI, configure your Domo API key and instance:

```bash
domo-vector configure
```

- Enter your Domo Developer API key when prompted.
- Enter your Domo instance name (e.g. `your-instance.domo.com`).
- This will create/update a `.env` file in the project directory with the necessary credentials.

---

## Usage

### Show Help

```bash
domo-vector help
```

---

## Quick Command Reference

### Configuration

- `domo-vector configure` - Set up API credentials and instance URL

### Vector Index Operations

- `domo-vector vector upload` - Upload and chunk files to vector index
- `domo-vector vector delete-all --index-id <id>` - Delete all nodes in index
- `domo-vector vector delete-by-id --index-id <id> --node-ids <id1> <id2>` - Delete specific nodes
- `domo-vector vector delete-by-group --index-id <id> --group-ids <group1>` - Delete nodes by group
- `domo-vector vector get-all --index-id <id>` - Get all node IDs

### Fileset Operations

- `domo-vector fileset create --name <name>` - Create new fileset
- `domo-vector fileset upload-file --fileset-id <id> --file-path <path>` - Upload file
- `domo-vector fileset upload-file --fileset-id <id> --directory <dir>` - Upload directory
- `domo-vector fileset get-file --fileset-id <id> --file-path <path>` - Download file
- `domo-vector fileset get-fileset --fileset-id <id>` - Get fileset metadata
- `domo-vector fileset get-filesets` - List all filesets
- `domo-vector fileset search-filesets` - Search filesets with pagination

---

### Vector Index Commands

**Index Types:**

- **Environment-specific indexes**: Indexes that are scoped to your current Domo environment

#### Upload Nodes (Chunk and Upload Files)

Upload text documents:

```bash
domo-vector vector upload --source-dir ./documentation --index-id your-index-id
```

Upload with image processing:

```bash
domo-vector vector upload --source-dir ./documentation --index-id your-index-id --include-images
```

**Options:**

- `--source-dir`: Source directory containing files (required)
- `--index-id`: ID for the vector index (optional if set in `.env` as `VECTOR_INDEX_ID`)
- `--include-images`: Process and embed image files along with text documents
- `--dry-run`: Preview what would be uploaded without actually uploading
- `--no-create-index`: Skip index creation, just upload to existing index
- `--chunk-size`: Maximum characters per text chunk (default: 1500)
- `--overlap`: Overlapping characters between chunks (default: 200)
- `--group-id`: Group ID for uploaded nodes (defaults to filename)

#### Delete Nodes by ID

```bash
domo-vector vector delete-by-id --index-id your-index-id --node-ids id1 id2 ...
```

#### Delete Nodes by Group

```bash
domo-vector vector delete-by-group --index-id your-index-id --group-ids group1 group2 ...
```

#### Delete All Nodes (without group)

```bash
domo-vector vector delete-all --index-id your-index-id
```

#### Get All Node IDs

```bash
domo-vector vector get-all --index-id your-index-id
```

---

### Fileset Commands

#### Create a Fileset

```bash
domo-vector fileset create --name "My Fileset" --description "Docs fileset"
```

#### Upload a File to a Fileset

```bash
domo-vector fileset upload-file --fileset-id <fileset-id> --file-path ./path/to/file.md
```

#### Upload an Entire Directory to a Fileset

```bash
domo-vector fileset upload-file --fileset-id <fileset-id> --directory ./path/to/docs
```

#### Download a File from a Fileset

```bash
domo-vector fileset get-file --fileset-id <fileset-id> --file-path <remote/path.md>
```

Or by file ID:

```bash
domo-vector fileset get-file --fileset-id <fileset-id> --file-id <file-id>
```

#### Get Fileset Metadata

```bash
domo-vector fileset get-fileset --fileset-id <fileset-id>
```

#### List All Filesets

```bash
domo-vector fileset get-filesets
```

#### Search Filesets

```bash
domo-vector fileset search-filesets --limit 10 --offset 0
```

- `--limit`: Maximum number of filesets to return (default: 10)
- `--offset`: Offset for pagination (default: 0)

---

## Supported File Types

### Text Documents

- Markdown (`.md`)
- JSON (`.json`)
- PDF (`.pdf`)
- HTML (`.html`)
- Plain text (`.txt`)

### Images (with `--include-images`)

- PNG (`.png`)
- JPEG (`.jpg`, `.jpeg`)
- GIF (`.gif`)
- BMP (`.bmp`)
- WebP (`.webp`)
- TIFF (`.tiff`)

---

## Development & Testing

- All source code is in the `domo_vector_cli/` directory.
- Tests are in the `tests/` directory. Run with:
  ```bash
  pytest
  ```
- For async test support, ensure `pytest-asyncio` is installed (already in requirements.txt).
- To check test coverage:
  ```bash
  pytest --cov=domo_vector_cli
  ```
- To update dependencies, edit `requirements.txt` and reinstall with `pip install -e .`

---

## Environment Variables

The CLI uses a `.env` file for configuration. Example:

```
DOMO_DEVELOPER_TOKEN=your-api-key-here
DOMO_API_URL_BASE=https://your-instance.domo.com/api
VECTOR_INDEX_ID=your-default-index-id
```

---

## Uninstall

To uninstall the CLI:

```bash
pip uninstall domo-vector
```

---

## License

MIT (or your chosen license)

---

## Troubleshooting

- If you see coroutine warnings, ensure `pytest-asyncio` is installed and you have reinstalled with `pip install -e .`.
- For API errors, check your `.env` values and Domo permissions.
- For more help, run:
  ```bash
  domo-vector help
  ```
