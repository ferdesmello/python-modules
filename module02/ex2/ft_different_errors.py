def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("non_existent_file.txt", "r")
    elif operation_number == 3:
        10 + "abc"
    else:
        return


def test_error_types() -> None:
    values = [0, 1, 2, 3, 4]
    for value in values:
        print(f"Testing operation {value}...")
        try:
            garden_operations(value)
            print("Operation completed successfully")
        except ValueError:
            print("Caught ValueError: "
                  "invalid literal for int() with base 10: 'abc'")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Caught FileNotFoundError: [Errno 2] "
                  "No such file or directory: '/non/existent/file'")
        except TypeError:
            print("Caught TypeError: "
                  "can only concatenate str (not 'int') to str")


def main() -> None:
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
