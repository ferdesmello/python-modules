class GardenPlant:
    def __init__(self,
                 init_name: str,
                 init_height: float,
                 init_age: int) -> None:
        self.p_name = init_name
        self.p_height = init_height
        self.p_age = init_age
        self.p_growth = 1.5
        if self.p_name.lower() == "cactus":
            self.p_growth = 0.5
        elif self.p_name.lower() == "sunflower":
            self.p_growth = 2.0

    def show(self) -> None:
        print(f"{self.p_name.capitalize()}: \
{round(self.p_height, 1)}cm, {self.p_age} days old")

    def grow(self) -> None:
        self.p_height += self.p_growth

    def age(self, days: int) -> None:
        for day in range(1, days + 1):
            print(f"=== Day {day} ===")
            self.p_age += 1
            self.grow()
            self.show()
        print(f"Growth this week: {days * self.p_growth}cm")


def main() -> None:
    garden = [
        GardenPlant("Rose", 25.0, 30),
        # GardenPlant("Sunflower", 80, 45),
        # GardenPlant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Growth ===")
    garden[0].show()
    garden[0].age(7)


if __name__ == "__main__":
    main()
