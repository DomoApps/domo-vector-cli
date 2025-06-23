import sys
import os
import pytest
import unittest.mock as mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from domo_vector_cli.upsert import (
    chunk_text_with_overlap,
    read_file_contents,
    iterate_documents_breadth_first,
    create_vector_index,
    upload_chunks_to_vector_index,
)
from domo_vector_cli.constants import (
    VectorOperation,
    IndexType,
    get_endpoint_key,
    ENDPOINT_MAPPING,
    ENDPOINTS,
)


def test_chunk_text_with_overlap_basic():
    text = "A B C D E F G H I J"
    chunks = chunk_text_with_overlap(text, max_length=5, overlap=2)
    assert isinstance(chunks, list)
    assert all(isinstance(c, str) for c in chunks)
    assert len(chunks) > 0


def test_read_file_contents(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("hello world")
    content = read_file_contents(str(file_path))
    assert content == "hello world"


def test_iterate_documents_breadth_first(tmp_path):
    d1 = tmp_path / "dir1"
    d1.mkdir()
    f1 = d1 / "a.md"
    f1.write_text("foo")
    f2 = tmp_path / "b.md"
    f2.write_text("bar")
    files = list(iterate_documents_breadth_first(str(tmp_path)))
    assert str(f1) in files
    assert str(f2) in files


def test_vector_operation_enum():
    """Test that VectorOperation enum has expected values."""
    assert VectorOperation.CREATE_INDEX.value == "create_index"
    assert VectorOperation.UPSERT_NODES.value == "upsert_nodes"
    assert VectorOperation.GET_INDEX.value == "get_index"
    assert VectorOperation.DELETE_INDEX.value == "delete_index"


def test_index_type_enum():
    """Test that IndexType enum has expected values."""
    assert IndexType.ENVIRONMENT.value == "environment"
    assert IndexType.GLOBAL.value == "global"


def test_get_endpoint_key_environment_operations():
    """Test get_endpoint_key for environment-specific operations."""
    # Test CREATE_INDEX for environment
    key = get_endpoint_key(VectorOperation.CREATE_INDEX, is_global=False)
    assert key == "create_index"

    # Test UPSERT_NODES for environment
    key = get_endpoint_key(VectorOperation.UPSERT_NODES, is_global=False)
    assert key == "upsert_nodes"

    # Test GET_INDEX for environment
    key = get_endpoint_key(VectorOperation.GET_INDEX, is_global=False)
    assert key == "get_index"

    # Test DELETE_INDEX for environment
    key = get_endpoint_key(VectorOperation.DELETE_INDEX, is_global=False)
    assert key == "delete_index"


def test_get_endpoint_key_global_operations():
    """Test get_endpoint_key for global operations."""
    # Test CREATE_INDEX for global
    key = get_endpoint_key(VectorOperation.CREATE_INDEX, is_global=True)
    assert key == "create_index_global"

    # Test UPSERT_NODES for global
    key = get_endpoint_key(VectorOperation.UPSERT_NODES, is_global=True)
    assert key == "upsert_nodes_global"


def test_get_endpoint_key_unsupported_global_operations():
    """Test that unsupported global operations raise KeyError."""
    # GET_INDEX is not supported for global indexes
    with pytest.raises(KeyError) as exc_info:
        get_endpoint_key(VectorOperation.GET_INDEX, is_global=True)

    assert "Unsupported operation 'get_index' for global index" in str(exc_info.value)
    assert "Supported operations:" in str(exc_info.value)

    # DELETE_INDEX is not supported for global indexes
    with pytest.raises(KeyError) as exc_info:
        get_endpoint_key(VectorOperation.DELETE_INDEX, is_global=True)

    assert "Unsupported operation 'delete_index' for global index" in str(
        exc_info.value
    )


def test_endpoint_mapping_completeness():
    """Test that ENDPOINT_MAPPING contains expected combinations."""
    # Environment-specific operations
    assert (IndexType.ENVIRONMENT, VectorOperation.CREATE_INDEX) in ENDPOINT_MAPPING
    assert (IndexType.ENVIRONMENT, VectorOperation.UPSERT_NODES) in ENDPOINT_MAPPING
    assert (IndexType.ENVIRONMENT, VectorOperation.GET_INDEX) in ENDPOINT_MAPPING
    assert (IndexType.ENVIRONMENT, VectorOperation.DELETE_INDEX) in ENDPOINT_MAPPING

    # Global operations (only CREATE_INDEX and UPSERT_NODES supported)
    assert (IndexType.GLOBAL, VectorOperation.CREATE_INDEX) in ENDPOINT_MAPPING
    assert (IndexType.GLOBAL, VectorOperation.UPSERT_NODES) in ENDPOINT_MAPPING

    # Global operations not supported
    assert (IndexType.GLOBAL, VectorOperation.GET_INDEX) not in ENDPOINT_MAPPING
    assert (IndexType.GLOBAL, VectorOperation.DELETE_INDEX) not in ENDPOINT_MAPPING


def test_endpoint_mapping_values():
    """Test that ENDPOINT_MAPPING returns correct endpoint keys."""
    # Environment-specific
    assert (
        ENDPOINT_MAPPING[(IndexType.ENVIRONMENT, VectorOperation.CREATE_INDEX)]
        == "create_index"
    )
    assert (
        ENDPOINT_MAPPING[(IndexType.ENVIRONMENT, VectorOperation.UPSERT_NODES)]
        == "upsert_nodes"
    )
    assert (
        ENDPOINT_MAPPING[(IndexType.ENVIRONMENT, VectorOperation.GET_INDEX)]
        == "get_index"
    )
    assert (
        ENDPOINT_MAPPING[(IndexType.ENVIRONMENT, VectorOperation.DELETE_INDEX)]
        == "delete_index"
    )

    # Global
    assert (
        ENDPOINT_MAPPING[(IndexType.GLOBAL, VectorOperation.CREATE_INDEX)]
        == "create_index_global"
    )
    assert (
        ENDPOINT_MAPPING[(IndexType.GLOBAL, VectorOperation.UPSERT_NODES)]
        == "upsert_nodes_global"
    )


@pytest.mark.asyncio
@mock.patch("httpx.AsyncClient")
@mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token"})
async def test_create_vector_index_uses_correct_endpoint(mock_client):
    """Test that create_vector_index uses the correct endpoint for global vs environment."""
    # Mock the response
    mock_response = mock.Mock()
    mock_response.json.return_value = {"success": True}
    mock_response.raise_for_status.return_value = None
    mock_client.return_value.__aenter__.return_value.post.return_value = mock_response

    # Test environment-specific index creation
    await create_vector_index("test-index", is_global=False)
    mock_client.return_value.__aenter__.return_value.post.assert_called_once()
    call_args = mock_client.return_value.__aenter__.return_value.post.call_args
    # The first positional argument should be the URL
    assert call_args[0][0] == ENDPOINTS["create_index"]

    # Reset mock
    mock_client.reset_mock()

    # Test global index creation
    await create_vector_index("test-index", is_global=True)
    mock_client.return_value.__aenter__.return_value.post.assert_called_once()
    call_args = mock_client.return_value.__aenter__.return_value.post.call_args
    # The first positional argument should be the URL
    assert call_args[0][0] == ENDPOINTS["create_index_global"]


@pytest.mark.asyncio
@mock.patch("httpx.AsyncClient")
@mock.patch.dict(os.environ, {"DOMO_DEVELOPER_TOKEN": "test_token"})
async def test_upload_chunks_uses_correct_endpoint(mock_client):
    """Test that upload_chunks_to_vector_index uses the correct endpoint."""
    # Mock the response
    mock_response = mock.Mock()
    mock_response.json.return_value = {"success": True}
    mock_response.raise_for_status.return_value = None
    mock_client.return_value.__aenter__.return_value.post.return_value = mock_response

    test_chunks = [{"text": "test content", "file_path": "test.md"}]

    # Test environment-specific upload
    await upload_chunks_to_vector_index(test_chunks, "test-index", is_global=False)
    mock_client.return_value.__aenter__.return_value.post.assert_called()
    call_args = mock_client.return_value.__aenter__.return_value.post.call_args
    expected_url = ENDPOINTS["upsert_nodes"].replace("{index_id}", "test-index")
    assert call_args[0][0] == expected_url

    # Reset mock
    mock_client.reset_mock()

    # Test global upload
    await upload_chunks_to_vector_index(test_chunks, "test-index", is_global=True)
    mock_client.return_value.__aenter__.return_value.post.assert_called()
    call_args = mock_client.return_value.__aenter__.return_value.post.call_args
    expected_url = ENDPOINTS["upsert_nodes_global"].replace("{index_id}", "test-index")
    assert call_args[0][0] == expected_url


def test_get_endpoint_key_default_behavior():
    """Test that get_endpoint_key defaults to environment-specific when is_global=False."""
    # Default behavior should be environment-specific
    key = get_endpoint_key(VectorOperation.CREATE_INDEX)
    assert key == "create_index"

    # Explicit False should also be environment-specific
    key = get_endpoint_key(VectorOperation.CREATE_INDEX, is_global=False)
    assert key == "create_index"
