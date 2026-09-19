import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]

    print("<=== Cyber Archives Recovery ===>")
    print(f"Accessing file '{filename}'")

    try:
        file_object: typing.IO[str] = open(filename, "r")
        fragments: str = file_object.read()

        print("---\n")
        print(fragments)
        print("\n---")

        file_object.close()
        print(f"File '{filename}' closed.")

    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")

    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
