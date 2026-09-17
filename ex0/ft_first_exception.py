#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    # except ValueError:
    except Exception:
        print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: '{temp_str}'")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature("25")
    print()
    test_temperature("abc")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
