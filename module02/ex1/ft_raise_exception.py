#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if 0 <= temp <= 40:
        return temp
    else:
        raise Exception("Temperature out of range", temp)


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError:
        print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: '{temp_str}'")
    except Exception as e:
        if e.args[1] < 0:
            print(f"Caught input_temperature error: "
                  f"{e.args[1]}°C is too cold for plants (min 0°C)")
        elif e.args[1] > 40:
            print(f"Caught input_temperature error: "
                  f"{e.args[1]}°C is too hot for plants (max 40°C)")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    test_temperature("-50")
    print()
    test_temperature("100")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
