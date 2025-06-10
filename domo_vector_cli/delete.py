import os
from domo_vector_cli.constants import ENDPOINTS


async def handle_delete_cli(args):
    if args.command == "delete-all":
        print(f"Deleting all nodes without group ids from index {args.index_id}")
        await delete_all_nodes_without_group_id(args.index_id)
        return
    if args.command == "delete-by-id":
        print(f"Deleting nodes by nodeId: {args.node_ids} from index {args.index_id}")
        result = await delete_nodes_by_id(args.index_id, args.node_ids)
        print(result)
    elif args.command == "delete-by-group":
        print(f"Deleting nodes by groupId: {args.group_ids} from index {args.index_id}")
        result = await delete_nodes_by_group_id(args.index_id, args.group_ids)
        print(result)


async def delete_all_nodes_without_group_id(index_id: str):
    """
    Deletes all nodes from the vector index by fetching all node IDs and calling the delete endpoint.
    """
    import httpx

    url_get = ENDPOINTS["get_index"].replace("{index_id}", index_id)
    headers = {"x-domo-developer-token": os.environ.get("DOMO_DEVELOPER_TOKEN", "")}
    async with httpx.AsyncClient() as client:
        print(f"Fetching all nodes from index {index_id}...")
        response = await client.post(url_get, json={}, headers=headers, timeout=60)
        response.raise_for_status()
        data = response.json()
        # Only delete nodes that do NOT have a groupId property
        node_ids = [
            node["id"] for node in data.get("nodes", []) if not node.get("groupId")
        ]

        if not node_ids:
            print(f"No nodes found in index {index_id} without groupId.")
            return
        print(f"Deleting {len(node_ids)} nodes from index {index_id}...")
        url_delete = ENDPOINTS["delete_index"].replace("{index_id}", index_id)
        payload = {"filter": {"nodeIds": node_ids}}
        del_response = await client.post(
            url_delete, json=payload, headers=headers, timeout=60
        )
        del_response.raise_for_status()
        print("Delete response:", del_response.json())
        return del_response.json()


async def delete_nodes_by_id(index_id: str, node_ids: list):
    """
    Deletes nodes from the vector index by nodeId list.
    """
    import httpx

    url = ENDPOINTS["delete_index"].replace("{index_id}", index_id)
    headers = {"x-domo-developer-token": os.environ.get("DOMO_DEVELOPER_TOKEN", "")}
    payload = {"nodeIds": node_ids}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()


async def delete_nodes_by_group_id(index_id: str, group_ids: list):
    """
    Deletes nodes from the vector index by nodeGroupId (groupId) list.
    """
    import httpx

    url = ENDPOINTS["delete_index"].replace("{index_id}", index_id)
    headers = {"x-domo-developer-token": os.environ.get("DOMO_DEVELOPER_TOKEN", "")}
    payload = {"nodeGroupIds": group_ids}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
