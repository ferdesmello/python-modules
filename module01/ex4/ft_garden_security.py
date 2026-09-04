class Plant:
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: int) -> None:
        self._p_name = init_name
        self._p_height = 0.0
        self._p_age = 0
        self._p_growth = 1.5
        if self._p_name.lower() == "cactus":
            self._p_growth = 0.5
        elif self._p_name.lower() == "sunflower":
            self._p_growth = 2.0
        elif self._p_name.lower() == "oak":
            self._p_growth = 1.0
        elif self._p_name.lower() == "fern":
            self._p_growth = 0.5

        if init_height < 0:
            print(f"{self._p_name.capitalize()}: "
                  f"Error, height can't be negative.")
            print("Height update rejected")
            self._p_height = 0.0
        else:
            self._p_height = init_height

        if init_age < 0:
            print(f"{self._p_name.capitalize()}: "
                  f"Error, age can't be negative.")
            print("Age update rejected")
            self._p_age = 0
        else:
            self._p_age = init_age

    def show(self) -> None:
        print(f"{self._p_name.capitalize()}: \
{round(self._p_height, 1)}cm, {self._p_age} days old")

    def grow(self) -> None:
        self._p_height += self._p_growth

    def age(self, days: int) -> None:
        for day in range(1, days + 1):
            print(f"=== Day {day} ===")
            self._p_age += 1
            self.grow()
            self.show()
        print(f"Growth this week: {days * self._p_growth}cm")

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._p_name.capitalize()}: "
                  f"Error, height can't be negative.")
            print("Height update rejected")
        else:
            self._p_height = new_height
            print(f"Height updated: {self._p_height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._p_name.capitalize()}: "
                  f"Error, age can't be negative.")
            print("Age update rejected")
        else:
            self._p_age = new_age
            print(f"Age updated: {self._p_age} days")

    def get_height(self) -> float:
        return self._p_height

    def get_age(self) -> int:
        return self._p_age


def main() -> None:
    garden = [
        Plant("Rose", 25.0, 30),
        # Plant("Sunflower", 80, 45),
        # Plant("Oak", 200, 1000),
        # Plant("Cactus", 15, 120),
        # Plant("Fern", 20, 300),
        # Plant("Palmtree", 100, 50)
    ]

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    garden[0].show()
    print()

    garden[0].set_height(50)
    garden[0].set_age(55)
    print()

    garden[0].set_height(-30)
    garden[0].set_age(-35)
    print()

    print("Current state: ", end="")
    garden[0].show()


if __name__ == "__main__":
    main()
