class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._p_grow_calls: int = 0
            self._p_age_calls: int = 0
            self._p_show_calls: int = 0

        def log_grow(self) -> None:
            self._p_grow_calls += 1

        def log_age(self) -> None:
            self._p_age_calls += 1

        def log_show(self) -> None:
            self._p_show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._p_grow_calls} grow, "
                f"{self._p_age_calls} age, "
                f"{self._p_show_calls} show"
            )

    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: float) -> None:
        self._p_name = init_name
        self._p_height = init_height
        self._p_age = init_age
        self._p_stats = self._Stats()

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
        self._p_stats.log_show()
        print(f"{self._p_name.capitalize()}: "
              f"{round(self._p_height, 1)}cm, {self._p_age} days old")

    def grow(self) -> None:
        self._p_stats.log_grow()
        self._p_height += self._p_growth

    def age(self, days: int) -> None:
        self._p_stats.log_age()
        self._p_age += days
        self._p_height += self._p_growth * days

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

    @staticmethod
    def year_age(age: float) -> bool:
        if age > 365:
            return True
        return False

    @classmethod
    def anonymous_plant(cls,
                        height: float = 0.0,
                        age: float = 0.0) -> "Plant":
        return cls("Unknown plant", height, age)


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


class Seed(Flower):
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: float,
                 color: str) -> None:
        super().__init__(init_name, init_height, init_age, color)
        self._seed: int = 0

    def bloom(self) -> None:
        if not self._blown:
            super().bloom()
            self._seed = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed}")


class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._p_shade_calls: int = 0

        def log_shade(self) -> None:
            self._p_shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._p_shade_calls} shade")

    _p_stats: _Stats

    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: float,
                 trunk_diameter: float) -> None:
        super().__init__(init_name, init_height, init_age)
        self._trunk_diameter = trunk_diameter
        self._shade_long = 0
        self._shade_wide = 0
        self._p_stats = self._Stats()

    def produce_shade(self) -> None:
        self._shade = True
        self._p_stats.log_shade()
        self._shade_long = 200
        self._shade_wide = 5

    def show(self) -> None:
        super().show()
        print(f" Trunk Diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: float,
                 harvest_season: str,
                 nutritional_value: float = 0.0) -> None:
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


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant._p_name.capitalize()}]")
    plant._p_stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.year_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.year_age(400)}")

    print("\n=== Flower")
    plant1 = Flower("Rose", 25.0, 30, "Red")
    plant1.show()
    display_plant_stats(plant1)
    plant1.grow()
    plant1.bloom()
    plant1.show()
    display_plant_stats(plant1)

    print("\n=== Tree")
    plant2 = Tree("Oak", 80, 45, 10.0)
    plant2.show()
    display_plant_stats(plant2)
    plant2.produce_shade()
    display_plant_stats(plant2)

    print("\n=== Seed")
    plant3 = Seed("Sunflower", 80, 20, "Yellow")
    plant3.show()
    display_plant_stats(plant3)
    plant3.grow()
    plant3.age(5)
    plant3.bloom()
    plant3.show()
    display_plant_stats(plant3)

    print("\n=== Anonymous")
    plant4 = Plant.anonymous_plant()
    plant4.show()
    display_plant_stats(plant4)


if __name__ == "__main__":
    main()
