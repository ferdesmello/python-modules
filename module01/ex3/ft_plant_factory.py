class Plant:
    def __init__(self,
                 start_name: str,
                 start_height: float,
                 start_age: int) -> None:
        self.p_name = start_name
        self.p_height = start_height
        self.p_age = start_age
        self.p_growth = 1.5
        if self.p_name.lower() == "cactus":
            self.p_growth = 0.5
        elif self.p_name.lower() == "sunflower":
            self.p_growth = 2.0
        elif self.p_name.lower() == "oak":
            self.p_growth = 1.0
        elif self.p_name.lower() == "fern":
            self.p_growth = 1.5

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
        Plant("Rose", 25.0, 30),
        Plant("Sunflower", 80, 45),
        Plant("Oak", 200, 1000),
        Plant("Cactus", 15, 120),
        Plant("Fern", 20, 300),
        Plant("Palmtree", 100, 50)
    ]

    print("=== Plant Factory Output ===")
    for plant in garden:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
