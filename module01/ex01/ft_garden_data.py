class GardenPlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name.capitalize()}: \
{self.height}cm, {self.age} days old")


def main():
    garden = [
        GardenPlant("Rose", 25, 30),
        GardenPlant("Sunflower", 80, 45),
        GardenPlant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    for plant in garden:
        plant.show()


if __name__ == "__main__":
    main()
