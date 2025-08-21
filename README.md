# Domo Vector CLI Tool

A Python CLI tool for chunking, uploading, and managing documentation files (Markdown, HTML, JSON, PDF) in a Domo vector index or fileset. Supports robust batching, error handling, retry logging, and configuration via `.env`.

---

## Features

### Vector Index Management

- Chunk and upload Markdown, HTML, JSON, and PDF files to a Domo vector index
- Robust batch uploads with error handling and retry logging (failed uploads are logged for retry)
- Delete nodes from a vector index:
  - By node ID (`vector delete-by-id`)
  - By group ID (`vector delete-by-group`)
  - Delete all nodes without a group (`vector delete-all`)
- Fetch all node IDs from an index (`vector get-all`)
- Configure your Domo API key and instance URL interactively

### Fileset Management

- Create new filesets
- Upload files or entire directories to filesets
- Download files from filesets
- Get fileset metadata and list files
- Search filesets by name or metadata
- Fetch file text content directly (without saving to disk)

- Comprehensive tests with async support

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd chunk-markdown
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

### Vector Index Commands

**Index Types:**

- **Environment-specific indexes**: Indexes that are scoped to your current Domo environment

#### Upload Nodes (Chunk and Upload Files)

**Environment-specific index:**

```bash
domo-vector vector upload --root ./documentation --index-id your-index-id
```

- `--root`: Root directory containing documentation files (default: `./documentation`)
- `--index-id`: ID for the vector index to create/use
- Additional options: `--dry-run`, `--no-create-index`, `--chunk-size`, `--overlap`, `--group-id`

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
domo-vector fileset upload-dir --fileset-id <fileset-id> --dir-path ./path/to/docs
```

#### Download a File from a Fileset

```bash
domo-vector fileset get-file --fileset-id <fileset-id> --file-path <remote/path.md>
```

#### Get Fileset Metadata

```bash
domo-vector fileset get-metadata --fileset-id <fileset-id>
```

#### List Files in a Fileset

```bash
domo-vector fileset list-files --fileset-id <fileset-id>
```

#### Search Filesets

```bash
domo-vector fileset search-filesets --name "search-term"
```

#### Fetch File Text Content

```bash
domo-vector fileset fetch-file-content --fileset-id <fileset-id> --file-path <remote/path.md>
```

---

## Supported File Types

- Markdown (`.md`)
- JSON (`.json`)
- PDF (`.pdf`)
- HTML (`.html`)

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
