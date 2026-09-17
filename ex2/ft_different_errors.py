#!/usr/bin/env python3
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "abc" + 10
    else:
        return


def test_error_types() -> None:
    values = [0, 1, 2, 3, 4]
    for value in values:
        print(f"Testing operation {value}...")
        try:
            garden_operations(value)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("\nMulti-Error Catching in a Single Try Block")
    for value in values:
        try:
            garden_operations(value)
            print("Operation completed successfully")
        except (ValueError,
                ZeroDivisionError,
                FileNotFoundError,
                TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
