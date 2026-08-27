class GardenPlant:
    def __init__(self, p_name: str, p_height: int, p_age: int) -> None:
        self.p_name = p_name
        self.p_height = p_height
        self.p_age = p_age
        self.p_growth = 1.5
        if self.p_name.lower() == "cactus":
            self.p_growth = 0.5
        elif self.p_name.lower() == "sunflower":
            self.p_growth = 2.0
        elif self.p_name.lower() == "oak":
            self.p_growth = 1.0
        elif self.p_name.lower() == "fern":
            self.p_growth = 0.5

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


def main():
    garden = [
        GardenPlant("Rose", 25.0, 30),
        GardenPlant("Sunflower", 80, 45),
        GardenPlant("Oak", 200, 1000),
        GardenPlant("Cactus", 15, 120),
        GardenPlant("Fern", 20, 300),
        GardenPlant("Palmtree", 100, 50)
    ]

    print("=== Plant Factory Output ===")
    for plant in garden:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()