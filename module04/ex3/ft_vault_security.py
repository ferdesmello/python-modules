def secure_archive(filename: str,
                   operation: str = 'r',
                   text: str = "") -> tuple[bool, str]:

    try:
        with open(filename, operation) as file_object:
            if operation == 'r':
                fragments: str = file_object.read()
                return True, fragments

            elif operation == 'w':
                file_object.write(text)
                print(f"Data saved in file '{filename}'.")
                return True, "Content successfully written to file"

            else:
                message = (f"Invalid operation '{operation}'."
                           f"Please use 'r' for read or 'w' for write.")
                return False, message

    except FileNotFoundError as e:
        return False, str(e)

    except PermissionError as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("blocked.txt", "r"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "r"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", "NEW CONTENT"))


if __name__ == "__main__":
    main()
