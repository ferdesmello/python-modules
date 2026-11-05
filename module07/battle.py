#! /usr/bin/env python3

from ex0 import CreatureFactory, FireCreatureFactory, WaterCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
        factory1: CreatureFactory, 
        factory2: CreatureFactory
    ) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())

    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    print("Testing factory")
    test_factory(FireCreatureFactory())

    print()
    print("Testing factory")
    test_factory(WaterCreatureFactory())

    print()
    print("Testing battle")
    test_battle(FireCreatureFactory(), WaterCreatureFactory())


if __name__ == "__main__":
    main()
