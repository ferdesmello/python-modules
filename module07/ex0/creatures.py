from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, creature_name: str, creature_type: str):
        self.creature_name = creature_name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self):
        pass

    def describe(self):
        return (
            f"{self.creature_name} is a "
            f"{self.creature_type} type Creature"
        )


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self):
        return (f"{self.creature_name} uses Ember!")


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self):
        return (f"{self.creature_name} uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self):
        return (f"{self.creature_name} uses Water Gun!")


class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self):
        return (f"{self.creature_name} uses Hydro Pump!")
