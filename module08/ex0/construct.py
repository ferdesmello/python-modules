#!/usr/bin/env python3
import sys
import os
import site


def main() -> None:
    base_prefix: str = getattr(sys, "base_prefix", "")
    real_prefix: str = getattr(sys, "real_prefix", "")
    env_prefix: str = getattr(sys, "prefix", "")

    in_venv: bool = (
        (base_prefix != "" and base_prefix != env_prefix)
        or (real_prefix != "" and real_prefix != env_prefix)
    )

    if not in_venv:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")

        print("Then run this program again.")

    else:
        print("MATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        env_name: str = os.path.basename(env_prefix)
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_prefix}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting"
              "\nthe global system.\n")

        site_packages: str = ""
        packages_paths = site.getsitepackages()
        if packages_paths:
            site_packages = packages_paths[0]
        print(f"Package installation path:"
              f"\n{site_packages}")


if __name__ == "__main__":
    main()
