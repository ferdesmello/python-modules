class Plant:
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: float) -> None:
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
            self._p_growth = 1.5

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
            print(f"{self._p_name.capitalize()}: \
Error, height can't be negative.")
            print("Height update rejected")
        else:
            print(f"Height updated: {self._p_height}cm")
            self._p_height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._p_name.capitalize()}: \
Error, age can't be negative.")
            print("Age update rejected")
        else:
            print(f"Age updated: {self._p_age} days")
            self._p_age = new_age

    def get_height(self) -> float:
        return self._p_height

    def get_age(self) -> float:
        return self._p_age


class Flower(Plant):
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: float,
                 color: str) -> None:
        super().__init__(init_name, init_height, init_age)
        self._color = color
        self._blown = False

    def get_color(self) -> str:
        return self._color

    def bloom(self) -> None:
        if not self._blown:
            self._blown = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blown:
            print(f" {self._p_name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._p_name.capitalize()} has not bloomed yet.")


class Tree(Plant):
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: float,
                 trunk_diameter: float) -> None:
        super().__init__(init_name, init_height, init_age)
        self._trunk_diameter = trunk_diameter
        self._shade = False
        self._shade_long = 0
        self._shade_wide = 0

    def produce_shade(self) -> None:
        if not self._shade:
            self._shade = True
            self._shade_long = 200
            self._shade_wide = 5
            print(f"{self._p_name.capitalize()} now produces a \
shade of {self._shade_long}cm long and {self._shade_wide}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk Diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: float,
                 harvest_season: str,
                 nutritional_value: float = 0) -> None:
        super().__init__(init_name, init_height, init_age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 2.5

    def age(self, days: int) -> None:
        super().age(days)

    def show(self) -> None:
        super().show()
        print(f" Harvest Season: {self._harvest_season.capitalize()}")
        print(f" Nutritional Value: {self._nutritional_value}")


def main():
    garden = [
        Flower("Rose", 25.0, 30, "Red"),
        Tree("Oak", 80, 45, 10.0),
        Vegetable("Carrot", 10, 2, "Fall"),
    ]

    print("=== Garden Plant Types ===")
    print("=== Flower")
    garden[0].show()
    garden[0].bloom()
    garden[0].show()

    print("\n=== Tree")
    garden[1].show()
    garden[1].produce_shade()

    print("\n=== Vegetable")
    garden[2].show()
    garden[2].age(5)
    garden[2].show()


if __name__ == "__main__":
    main()
