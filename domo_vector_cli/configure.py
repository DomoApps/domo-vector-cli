import os


def handle_configure_cli():
    """
    Prompts the user for their Domo Developer Token and API URL base, then writes them to a .env file.
    """
    print("Configure Domo Vector CLI")
    token = input("Enter your DOMO_DEVELOPER_TOKEN: ").strip()
    instance = input("Enter your Domo instance (e.g. acme.domo.com): ").strip()
    index_id = input(
        "Enter your default VECTOR_INDEX_ID (e.g. partner-gpt-index): "
    ).strip()
    # Validate input: must end with .domo.com and not contain protocol or /api
    if (
        not instance.endswith(".domo.com")
        or "/" in instance
        or instance.startswith("http")
    ):
        print(
            "Invalid instance. Please enter only the subdomain and domain, e.g. acme.domo.com"
        )
        return
    url_base = f"https://{instance}/api"
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    with open(env_path, "w") as f:
        f.write(f"DOMO_DEVELOPER_TOKEN={token}\n")
        f.write(f"DOMO_API_URL_BASE={url_base}\n")
        f.write(f"VECTOR_INDEX_ID={index_id}\n")
    print(f".env file written to {env_path}")
