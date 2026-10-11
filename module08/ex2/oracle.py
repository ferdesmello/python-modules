#!/usr/bin/env python3
import sys
<<<<<<< HEAD
import os
from dotenv import load_dotenv
=======

try:
    from dotenv import load_dotenv
    loaded_dotenv: bool = True
except ImportError:
    loaded_dotenv = False
>>>>>>> 0d4e642 (ajustes finais)


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    if loaded_dotenv is False:
        print(
            'python-dotenv is missing. Install it with '
            'pip install -r requirements.txt'
        )
        sys.exit(1)

    load_dotenv()

    matrix_mode: str | None = os.getenv("MATRIX_MODE")
    db_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    log_level: str | None = os.getenv("LOG_LEVEL")
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

    if matrix_mode is not None:
        matrix_mode = matrix_mode.lower()

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
        status: str = "Authenticated"
        if api_key and api_key == "test":
            status = "Test Key (Limited Access)"
        elif not api_key:
            status = "Not Authenticated"
        print(f"API Access: {status}")
    else:
        print("API Access: [MISSING] Unauthenticated")

    print(f"Log Level: {log_level}")

    if zion_endpoint and zion_endpoint.startswith("http"):
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline / Invalid URL")

    print("\nEnvironment security check:")
    with open(__file__, "r") as f:
        content = f.read()
        if (api_key and api_key in content) or (db_url and db_url in content):
            print("[WARNING] Hardcoded secrets detected in the code!")
            sys.exit(1)
        else:
            print("[OK] No hardcoded secrets detected")

    env_exists: bool = os.path.exists(".env")
    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found (using system environment)")

<<<<<<< HEAD
    if matrix_mode == "production":
        print("[OK] Running with Production overrides active")
    else:
=======
    if any([matrix_mode, db_url, api_key, log_level, zion_endpoint]):
>>>>>>> 0d4e642 (ajustes finais)
        print("[OK] Production overrides available")
    else:
        print("[INFO] Environment variable override not active")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
