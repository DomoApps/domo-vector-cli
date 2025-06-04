import os
from constants import API_URL_BASE


async def handle_get_cli(args):
    """
    Handles the 'get' command for the CLI, fetching all node IDs from the specified index.
    """
    if args.command == "get-all":
        print(f"Fetching all node IDs from index {args.index_id}...")
        node_ids = await get_all_node_ids(args.index_id)
        print(f"Node IDs in index {args.index_id}: {node_ids}")
    else:
        print("Unknown command. Use 'get-all' to fetch all node IDs.")


async def get_all_node_ids(index_id: str) -> list:
    """
    Fetches all node IDs from the vector index using the /get endpoint.
    """
    import httpx

    url = f"{API_URL_BASE}/recall/v1/indexes/{index_id}/get"
    headers = {"x-domo-developer-token": os.environ.get("DOMO_DEVELOPER_TOKEN", "")}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json={}, headers=headers)
        response.raise_for_status()
        data = response.json()
        return [node["id"] for node in data.get("nodes", [])]
