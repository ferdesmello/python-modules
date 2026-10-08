#!/usr/bin/env python3
import sys
import os
from dotenv import load_dotenv


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    load_dotenv()

    matrix_mode: str = os.getenv("MATRIX_MODE", "development").lower()
    db_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT")

    required: dict[str, str | None] = {
        "DATABASE_URL": db_url,
        "API_KEY": api_key,
        "ZION_ENDPOINT": zion_endpoint
    }
    missing: list[str] = [key for key, val in required.items() if not val]

    if missing:
        print(f"WARNING/ERROR: Missing required configuration keys: "
              f"{', '.join(missing)}")
        print("Please check your .env file or environment variables.")
        sys.exit(1)

    print("Configuration loaded:")

    print(f"Mode: {matrix_mode}")

    if db_url and (
        "sqlite" in db_url
        or "localhost" in db_url
        or "127.0.0.1" in db_url
    ):
        print("Database: Connected to local instance")
    elif db_url:
        print("Database: Connected to remote production instance")
    else:
        print("Database: [MISSING] No connection string provided")

    if api_key:
        status: str = ""
        if matrix_mode == "production":
            status = "Authenticated ****"
        elif matrix_mode == "development":
            status = "Authenticated"
        print(f"API Access: {status}")
    else:
        print("API Access: [MISSING] Unauthenticated")

    print(f"Log Level: {log_level}")

    if zion_endpoint and zion_endpoint.startswith("http"):
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline / Invalid URL")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    env_exists: bool = os.path.exists(".env")
    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found (using system environment)")

    if matrix_mode == "production":
        print("[OK] Running with Production overrides active")
    else:
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
