#! /usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from typing import cast


def main() -> None:
    print("Testing Creature with healing capability")
    healing_factory = HealingCreatureFactory()

    print(" base:")
    base_heal = healing_factory.create_base()
    print(base_heal.describe())
    print(base_heal.attack())
    print(cast(HealCapability, base_heal).heal())

    print(" evolved:")
    evolved_heal = healing_factory.create_evolved()
    print(evolved_heal.describe())
    print(evolved_heal.attack())
    print(cast(HealCapability, evolved_heal).heal())

    print()
    print("Testing Creature with transform capability")
    transform_factory = TransformCreatureFactory()

    print(" base:")
    base_trans = transform_factory.create_base()
    print(base_trans.describe())
    print(base_trans.attack())
    print(cast(TransformCapability, base_trans).transform())
    print(base_trans.attack())
    print(cast(TransformCapability, base_trans).revert())

    print(" evolved:")
    evolved_trans = transform_factory.create_evolved()
    print(evolved_trans.describe())
    print(evolved_trans.attack())
    print(cast(TransformCapability, evolved_trans).transform())
    print(evolved_trans.attack())
    print(cast(TransformCapability, evolved_trans).revert())


if __name__ == "__main__":
    main()
