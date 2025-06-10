# Domo Vector CLI Tool

A Python CLI tool for chunking, uploading, and managing documentation files (Markdown, HTML, JSON, PDF) in a Domo vector index. Supports robust batching, error handling, and configuration via `.env`.

---

## Features

- Chunk and upload Markdown, HTML, JSON, and PDF files to a Domo vector index
- Batch uploads with error handling and logging
- Delete nodes by ID, group, or all
- Fetch all node IDs from an index
- Configure your Domo API key and instance URL interactively

---

## Installation

1. **Clone the repository:**

   ```fish
   git clone <your-repo-url>
   cd chunk-markdown
   ```

2. **Install dependencies and the CLI tool locally:**
   ```fish
   pip install -e .
   ```
   This will make the `domo-vector` command available globally.

---

## Configuration

Before using the CLI, configure your Domo API key and instance:

```fish
domo-vector configure
```

- Enter your Domo Developer API key when prompted.
- Enter your Domo instance name (e.g. `your-instance.domo.com`).
- This will create/update a `.env` file in the project directory with the necessary credentials.

---

## Usage

### Show Help

```fish
domo-vector help
```

### Upload Nodes (Chunk and Upload Files)

```fish
domo-vector upload-nodes --root ./documentation --index-id your-index-id
```

- `--root`: Root directory containing documentation files (default: `./documentation`)
- `--index-id`: ID for the vector index to create/use
- Additional options: `--dry-run`, `--no-create-index`, `--chunk-size`, `--overlap`, `--group-id`

### Delete Nodes by ID

```bash
domo-vector delete-by-id --index-id your-index-id --node-ids id1 id2 ...
```

### Delete Nodes by Group

```bash
domo-vector delete-by-group --index-id your-index-id --group-ids group1 group2 ...
```

### Delete All Nodes (without group)

```bash
domo-vector delete-all --index-id your-index-id
```

### Get All Node IDs

```bash
domo-vector get-all --index-id your-index-id
```

---

## Supported File Types

- Markdown (`.md`)
- JSON (`.json`)

Coming Soon

- PDF (`.pdf`)
- HTML (`.html`)

---

## Development & Testing

- All source code is in the project root.
- Tests are in the `tests/` directory. Run with:
  ```fish
  pytest
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

```fish
pip uninstall domo-vector
```

---

## License

MIT (or your chosen license)

---

## Troubleshooting

- If you see coroutine warnings, ensure your `setup.py` entry point is `main:main` and you have reinstalled with `pip install -e .`.
- For API errors, check your `.env` values and Domo permissions.
- For more help, run:
  ```fish
  domo-vector help
  ```
