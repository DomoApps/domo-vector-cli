import pytest
import argparse
import sys
import os
from unittest import mock
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from domo_vector_cli import fileset


class TestFilesetEndpoints:
    """Test that fileset functions use correct endpoints."""

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    @mock.patch('domo_vector_cli.fileset.requests.post')
    def test_create_fileset_endpoint(self, mock_post):
        # Arrange
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"id": "fs123", "name": "Test Fileset"}
        mock_post.return_value = mock_response

        # Act
        result = fileset.create_fileset("Test Fileset", "Test Description")

        # Assert
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args[0][0] == "https://test.domo.com/api/files/v1/filesets"
        assert call_args[1]["json"]["name"] == "Test Fileset"
        assert call_args[1]["json"]["description"] == "Test Description"
        assert result["id"] == "fs123"

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    @mock.patch('domo_vector_cli.fileset.requests.post')
    def test_get_all_filesets_endpoint(self, mock_post):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "fileSets": [{"id": "fs1", "name": "Fileset 1"}, {"id": "fs2", "name": "Fileset 2"}],
            "pageContext": {"count": 2, "totalCount": 2, "offset": 0}
        }
        mock_post.return_value = mock_response

        # Act
        result = fileset.get_all_filesets()

        # Assert
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args[0][0] == "https://test.domo.com/api/files/v1/filesets/search"
        # Verify the payload structure
        assert "json" in call_args[1]
        payload = call_args[1]["json"]
        assert "fieldSort" in payload
        assert "filters" in payload
        assert "dateFilters" in payload
        assert result["success"] is True
        assert len(result["filesets"]) == 2

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    @mock.patch('domo_vector_cli.fileset.requests.get')
    def test_get_fileset_metadata_endpoint(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "fs123", "name": "Test Fileset", "fileCount": 5}
        mock_get.return_value = mock_response

        # Act
        result = fileset.get_fileset_metadata("fs123")

        # Assert
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert call_args[0][0] == "https://test.domo.com/api/files/v1/filesets/fs123"
        assert result["success"] is True
        assert result["fileset"]["fileCount"] == 5

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    @mock.patch('domo_vector_cli.fileset.requests.post')
    def test_search_filesets_endpoint(self, mock_post):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"filesets": [{"id": "fs1", "name": "Search Result"}]}
        mock_post.return_value = mock_response

        # Act
        result = fileset.search_filesets(limit=5, offset=10)

        # Assert
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args[0][0] == "https://test.domo.com/api/files/v1/filesets/search?limit=5&offset=10"
        assert result["success"] is True


class TestFilesetFunctionality:
    """Test fileset function business logic."""

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    @mock.patch('domo_vector_cli.fileset.requests.post')
    def test_create_fileset_with_defaults(self, mock_post):
        # Arrange
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"id": "fs123"}
        mock_post.return_value = mock_response

        # Act
        result = fileset.create_fileset("My Fileset")

        # Assert
        call_args = mock_post.call_args
        body = call_args[1]["json"]
        assert body["name"] == "My Fileset"
        assert body["aiEnabled"] is True
        assert body["batchType"] == "INCREMENTAL"
        assert body["connector"] == "DOMO"

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    @mock.patch('domo_vector_cli.fileset.requests.post')
    def test_get_all_filesets_error_handling(self, mock_post):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_post.return_value = mock_response

        # Act
        result = fileset.get_all_filesets()

        # Assert
        assert result["success"] is False
        assert result["status_code"] == 404
        assert result["error"] == "Not Found"

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    @mock.patch('domo_vector_cli.fileset.requests.post')
    def test_search_filesets_with_custom_params(self, mock_post):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"filesets": []}
        mock_post.return_value = mock_response

        # Act
        custom_filters = [{"field": "name", "value": "test"}]
        custom_sort = [{"field": "createdAt", "order": "ASC"}]
        result = fileset.search_filesets(
            limit=20, 
            offset=5, 
            filters=custom_filters,
            field_sort=custom_sort
        )

        # Assert
        call_args = mock_post.call_args
        body = call_args[1]["json"]
        assert body["filters"] == custom_filters
        assert body["fieldSort"] == custom_sort

    def test_create_fileset_missing_token(self):
        # Arrange
        with mock.patch.dict(os.environ, {}, clear=True):
            # Act & Assert
            with pytest.raises(RuntimeError, match="DOMO_DEVELOPER_TOKEN environment variable not set"):
                fileset.create_fileset("Test")


class TestFileUpload:
    """Test file upload functionality."""

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    def test_upload_file_to_fileset_success(self):
        # Since the upload_file_to_fileset function is complex with file I/O and logging,
        # we'll test that it calls the correct endpoint with proper parameters
        with mock.patch('os.path.getsize', return_value=100):
            with mock.patch('os.path.basename', return_value="file.txt"):
                with mock.patch('mimetypes.add_type'):  # Mock the mimetypes call
                    with mock.patch('builtins.open', mock.mock_open(read_data="test content")):
                        with mock.patch('domo_vector_cli.fileset.requests.post') as mock_post:
                            mock_response = MagicMock()
                            mock_response.ok = True
                            mock_response.json.return_value = {"id": "file123"}
                            mock_post.return_value = mock_response

                            # Act
                            result = fileset.upload_file_to_fileset("fs123", "/path/to/file.txt", "documents/")

                            # Assert
                            mock_post.assert_called_once()
                            call_args = mock_post.call_args
                            assert "fs123" in call_args[0][0]  # URL contains fileset_id
                            assert result["id"] == "file123"

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    @mock.patch('os.path.getsize')
    def test_upload_file_skip_empty_file(self, mock_getsize):
        # Arrange
        mock_getsize.return_value = 0  # Empty file

        # Act
        result = fileset.upload_file_to_fileset("fs123", "/path/to/empty.txt", "")

        # Assert
        assert result["skipped"] is True
        assert result["reason"] == "empty file"


class TestFileDownload:
    """Test file download functionality."""

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    @mock.patch('domo_vector_cli.fileset.requests.get')
    def test_get_file_from_fileset_by_path(self, mock_get):
        # Arrange
        # Mock the path query response
        path_response = MagicMock()
        path_response.status_code = 200
        path_response.json.return_value = {"id": "file123", "name": "test.txt"}
        
        # Mock the download response
        download_response = MagicMock()
        download_response.status_code = 200
        download_response.iter_content.return_value = [b"file content"]
        
        mock_get.side_effect = [path_response, download_response]

        # Act
        with mock.patch('builtins.open', mock.mock_open()) as mock_file:
            result = fileset.get_file_from_fileset("fs123", file_path="documents/test.txt")

        # Assert
        assert mock_get.call_count == 2
        assert result["success"] is True

    @mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token", "DOMO_API_URL_BASE": "https://test.domo.com/api"})
    def test_get_file_from_fileset_no_params(self):
        # Act
        result = fileset.get_file_from_fileset("fs123")

        # Assert
        assert result["success"] is False
        assert "No file_path or file_id provided" in result["error"]


class TestCLIHandlers:
    """Test CLI command handlers."""

    @pytest.mark.asyncio
    async def test_handle_fileset_cli_create(self, capsys):
        # Arrange
        mock_args = MagicMock()
        mock_args.fileset_command = "create"
        mock_args.name = "Test Fileset"
        mock_args.description = "Test Description"

        with mock.patch('domo_vector_cli.fileset.create_fileset') as mock_create:
            mock_create.return_value = {"id": "fs123", "name": "Test Fileset"}

            # Act
            await fileset.handle_fileset_cli(mock_args)

        # Assert
        mock_create.assert_called_once_with(name="Test Fileset", description="Test Description")
        captured = capsys.readouterr()
        assert "Fileset created" in captured.out

    @pytest.mark.asyncio
    async def test_handle_fileset_cli_get_filesets(self, capsys):
        # Arrange
        mock_args = MagicMock()
        mock_args.fileset_command = "get-filesets"

        with mock.patch('domo_vector_cli.fileset.get_all_filesets') as mock_get:
            mock_get.return_value = {
                "success": True,
                "filesets": [{"id": "fs1", "name": "Fileset 1"}, {"id": "fs2", "name": "Fileset 2"}]
            }

            # Act
            await fileset.handle_fileset_cli(mock_args)

        # Assert
        mock_get.assert_called_once()
        captured = capsys.readouterr()
        assert "Found 2 filesets" in captured.out
        assert "Fileset 1" in captured.out

    @pytest.mark.asyncio
    async def test_handle_fileset_cli_get_fileset(self, capsys):
        # Arrange
        mock_args = MagicMock()
        mock_args.fileset_command = "get-fileset"
        mock_args.fileset_id = "fs123"

        with mock.patch('domo_vector_cli.fileset.get_fileset_metadata') as mock_get:
            mock_get.return_value = {
                "success": True,
                "fileset": {
                    "id": "fs123",
                    "name": "Test Fileset",
                    "description": "Test Description",
                    "fileCount": 5
                }
            }

            # Act
            await fileset.handle_fileset_cli(mock_args)

        # Assert
        mock_get.assert_called_once_with("fs123")
        captured = capsys.readouterr()
        assert "Test Fileset" in captured.out
        assert "File count: 5" in captured.out

    @pytest.mark.asyncio
    async def test_handle_fileset_cli_upload_file(self, capsys):
        # Arrange
        class MockArgs:
            fileset_command = "upload-file"
            fileset_id = "fs123"
            file_path = "/path/to/file.txt"
            directory = None
        
        mock_args = MockArgs()

        with mock.patch('domo_vector_cli.fileset.upload_file_to_fileset') as mock_upload:
            mock_upload.return_value = {"id": "file123"}

            # Act
            await fileset.handle_fileset_cli(mock_args)

        # Assert
        mock_upload.assert_called_once_with("fs123", "/path/to/file.txt", "")
        captured = capsys.readouterr()
        assert "Uploading file" in captured.out

    @pytest.mark.asyncio
    async def test_handle_fileset_cli_upload_directory(self, capsys):
        # Arrange
        mock_args = MagicMock()
        mock_args.fileset_command = "upload-file"
        mock_args.fileset_id = "fs123"
        mock_args.directory = "/path/to/docs"
        mock_args.file_path = None

        with mock.patch('domo_vector_cli.fileset.upload_directory_to_fileset') as mock_upload_dir:
            with mock.patch('os.path.isdir', return_value=True):
                # Act
                await fileset.handle_fileset_cli(mock_args)

        # Assert
        mock_upload_dir.assert_called_once_with("fs123", "/path/to/docs")

    @pytest.mark.asyncio
    async def test_handle_fileset_cli_search_filesets(self, capsys):
        # Arrange
        mock_args = MagicMock()
        mock_args.fileset_command = "search-filesets"
        mock_args.limit = 5
        mock_args.offset = 10

        with mock.patch('domo_vector_cli.fileset.search_filesets') as mock_search:
            mock_search.return_value = {
                "success": True,
                "filesets": [{"id": "fs1", "name": "Search Result"}]
            }

            # Act
            await fileset.handle_fileset_cli(mock_args)

        # Assert
        mock_search.assert_called_once_with(limit=5, offset=10)
        captured = capsys.readouterr()
        assert "Found 1 filesets" in captured.out

    @pytest.mark.asyncio
    async def test_handle_fileset_cli_unknown_command(self, capsys):
        # Arrange
        mock_args = MagicMock()
        mock_args.fileset_command = "unknown-command"

        # Act
        await fileset.handle_fileset_cli(mock_args)

        # Assert
        captured = capsys.readouterr()
        assert "Unknown fileset command" in captured.out


class TestArgumentParsing:
    """Test that fileset commands are properly parsed."""

    def test_fileset_create_args_parsing(self):
        """Test that create command args are parsed correctly."""
        # This would be integration test with main.py
        # Testing that the argument structure matches what CLI expects
        from domo_vector_cli.constants import COMMANDS
        
        create_cmd = COMMANDS["fileset"]["subcommands"]["create"]
        assert create_cmd["help"] == "Create a new Fileset"
        
        # Check required args
        name_arg = next(arg for arg in create_cmd["args"] if arg["name"] == "--name")
        assert name_arg["required"] is True
        
        # Check optional args  
        desc_arg = next(arg for arg in create_cmd["args"] if arg["name"] == "--description")
        assert desc_arg["required"] is False