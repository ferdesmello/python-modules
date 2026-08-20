class GardenPlant:
    def __init__(self, p_name: str, p_height: int, p_age: int):
        self.p_name = p_name
        self.p_height = p_height
        self.p_age = p_age
        self.p_growth = 1.5

    def show(self):
        print(f"{self.p_name.capitalize()}: \
{round(self.p_height, 1)}cm, {self.p_age} days old")

    def grow(self):
        self.p_height += self.p_growth

    def age(self, days: int):
        for day in range(1, days + 1):
            print(f"=== Day {day} ===")
            self.p_age += 1
            self.grow()
            self.show()
        print(f"Growth this week: {days * self.p_growth}cm")


def main():
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
