class GardenPlant:
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: int) -> None:
        self._p_name = init_name
        self._p_height = init_height
        self._p_age = init_age
        self._p_growth = 1.5
        if self._p_name.lower() == "cactus":
            self._p_growth = 0.5
        elif self._p_name.lower() == "sunflower":
            self._p_growth = 2.0
        elif self._p_name.lower() == "oak":
            self._p_growth = 1.0
        elif self._p_name.lower() == "fern":
            self._p_growth = 0.5

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

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._p_name}: Error, height can't be negative.")
            print("Height update rejected")
        else:
            print(f"Height updated: {self._p_height}cm")
            self._p_height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._p_name}: Error, age can't be negative.")
            print("Age update rejected")
        else:
            print(f"Age updated: {self._p_age} days")
            self._p_age = age

    def get_height(self) -> float:
        return self._p_height

    def get_age(self) -> int:
        return self._p_age


def main() -> None:
    garden = [
        GardenPlant("Rose", 25.0, 30),
        # GardenPlant("Sunflower", 80, 45),
        # GardenPlant("Oak", 200, 1000),
        # GardenPlant("Cactus", 15, 120),
        # GardenPlant("Fern", 20, 300),
        # GardenPlant("Palmtree", 100, 50)
    ]

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    garden[0].show()

    garden[0].set_height(50)
    garden[0].set_age(55)
    print("Current state: ", end="")
    garden[0].show()

    garden[0].set_height(-30)
    garden[0].set_age(-35)
    print("Current state: ", end="")
    garden[0].show()


if __name__ == "__main__":
    main()
