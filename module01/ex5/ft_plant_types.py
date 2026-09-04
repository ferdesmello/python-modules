class Plant:
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: float) -> None:
        self._p_name = init_name
        self._p_height = 0.0
        self._p_age = 0.0
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
            self._p_age = 0.0
        else:
            self._p_age = init_age

    def show(self) -> None:
        print(f"{self._p_name.capitalize()}: \
{round(self._p_height, 1)}cm, {self._p_age} days old")

    def grow(self, days: int) -> None:
        self._p_height += self._p_growth * days

    def age(self, days: int) -> None:
        self._p_age += days

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
            print(f" {self._p_name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: float,
                 trunk_diameter: float) -> None:
        super().__init__(init_name, init_height, init_age)
        self._trunk_diameter = trunk_diameter
        self._shade: bool = False
        self._shade_long: float = 0.0
        self._shade_wide: float = 0.0

    def produce_shade(self) -> None:
        if not self._shade:
            self._shade = True
            self._shade_long = 200.0
            self._shade_wide = 5.0
            print(f"Tree {self._p_name.capitalize()} now produces a "
                  f"shade of {round(self._shade_long, 1)}cm long and "
                  f"{round(self._shade_wide, 1)}cm wide.")

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

    def grow(self, days: int) -> None:
        super().grow(days)
        self._nutritional_value += self._nutritional_value + 1.5 * days

    def age(self, days: int) -> None:
        super().age(days)

    def show(self) -> None:
        super().show()
        print(f" Harvest Season: {self._harvest_season.capitalize()}")
        print(f" Nutritional Value: {round(self._nutritional_value, 1)}")


def main() -> None:
    plant1 = Flower("Rose", 25.0, 30, "Red")
    plant2 = Tree("Oak", 80.0, 45, 10.0)
    plant3 = Vegetable("Carrot", 10.0, 2, "Fall")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant1.show()
    plant1.bloom()
    plant1.show()

    print("\n=== Tree")
    plant2.show()
    plant2.produce_shade()

    print("\n=== Vegetable")
    plant3.show()
    plant3.grow(20)
    plant3.age(20)
    plant3.show()


if __name__ == "__main__":
    main()
