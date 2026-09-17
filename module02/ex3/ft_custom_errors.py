#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def plant_health(good_health: bool) -> None:
    if not good_health:
        raise PlantError("The tomato plant is wilting!")


def plant_water(liters: int) -> None:
    if liters < 5:
        raise WaterError("Not enough water in the tank!")


def test_error() -> None:
    print("Testing PlantError...")
    try:
        plant_health(False)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        plant_water(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        plant_health(False)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        plant_water(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    test_error()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
