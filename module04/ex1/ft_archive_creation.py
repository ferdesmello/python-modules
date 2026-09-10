import sys
import typing


def read_fragments(filename: str) -> str | None:
    try:
        file_object: typing.IO[str] = open(filename, "r")
        fragments: str = file_object.read()

        print("---\n")
        print(fragments)
        print("\n---")

        file_object.close()
        print(f"File '{filename}' closed.")

        return fragments

    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
        return None

    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")
        return None

    finally:
        if file_object is not None:
            file_object.close()


def change_fragments(fragments: str) -> str:
    lines: list[str] = fragments.splitlines()
    changed_lines: list[str] = [f"{line}#" for line in lines]
    new_fragments: str = ("\n".join(changed_lines) +
                          "\n" if changed_lines else "")

    print("---\n")
    print(new_fragments)
    print("\n---")

    return new_fragments


def save_new_fragments(new_filename: str, new_fragments: str) -> None:
    try:
        print(f"Saving data to '{new_filename}'")
        file_obj: typing.IO[str] = open(new_filename, "w")
        file_obj.write(new_fragments)
        file_obj.close()
        print(f"Data saved in file '{new_filename}'.")

    except Exception as e:
        print(f"Error writing to file '{new_filename}': {e}")
        print("Not saving data.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")

    print("<=== Cyber Archives Recovery & Preservation ===>")

    fragments: str | None = read_fragments(filename)
    if fragments is None:
        return

    print("\nTransform data:")
    new_fragments: str = change_fragments(fragments)
    new_filename: str = input("Enter new file name (or empty): ")
    if not new_filename:
        print("Not saving data.")
        return

    save_new_fragments(new_filename, new_fragments)


if __name__ == "__main__":
    main()
