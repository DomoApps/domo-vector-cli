import os


def handle_configure_cli():
    """
    Prompts the user for their Domo Developer Token and API URL base, then writes them to a .env file.
    """
    print("\n=== Domo Vector CLI Configuration ===")
    print("Please provide your Domo credentials and settings:\n")
    
    token = input("Enter your DOMO_DEVELOPER_TOKEN: ").strip()
    if not token:
        print("ERROR: Developer token is required.")
        return
        
    instance = input("Enter your Domo instance (e.g. acme.domo.com): ").strip()
    if not instance:
        print("ERROR: Domo instance is required.")
        return
        
    index_id = input("Enter your default VECTOR_INDEX_ID (optional, press Enter to skip): ").strip()
    
    # Validate input: must end with .domo.com and not contain protocol or /api
    if (
        not instance.endswith(".domo.com")
        or "/" in instance
        or instance.startswith("http")
    ):
        print("\nERROR: Invalid instance format.")
        print("Please enter only the subdomain and domain, e.g. 'acme.domo.com'")
        print("Do not include 'https://' or '/api'")
        return
    
    url_base = f"https://{instance}/api"
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    
    try:
        with open(env_path, "w") as f:
            f.write(f"DOMO_DEVELOPER_TOKEN={token}\n")
            f.write(f"DOMO_API_URL_BASE={url_base}\n")
            if index_id:
                f.write(f"VECTOR_INDEX_ID={index_id}\n")
        
        print(f"\n✅ Configuration saved successfully!")
        print(f"📁 Created .env file at: {env_path}")
        print(f"🔗 API Base URL: {url_base}")
        if index_id:
            print(f"📊 Default Index ID: {index_id}")
        print("\nYou can now run vector and fileset commands!")
        print("Example: domo-vector vector upload --source-dir ./my-docs")
        
    except Exception as e:
        print(f"\nERROR: Failed to write configuration file: {e}")
        print("Please check file permissions and try again.")
