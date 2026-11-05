#! /usr/bin/env python3

from typing import List, Tuple
from ex0 import CreatureFactory, FireCreatureFactory, WaterCreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


Opponent = Tuple[CreatureFactory, BattleStrategy]

def battle(opponents: List[Opponent]) -> None:
    """Organize tournament fights between opponents."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            f1, s1 = opponents[i]
            f2, s2 = opponents[j]

            c1 = f1.create_base()
            c2 = f2.create_base()

            print("\n* Battle *")
            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")

            try:
                s1.act(c1)
                s2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    """Run all Exercise 2 tournament tests."""
    fire_factory = FireCreatureFactory()
    water_factory = WaterCreatureFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(fire_factory, normal_strat), (healing_factory, defensive_strat)])

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(
        [(fire_factory, aggressive_strat), (healing_factory, defensive_strat)]
    )

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(
        [
            (water_factory, normal_strat),
            (healing_factory, defensive_strat),
            (transform_factory, aggressive_strat),
        ]
    )


if __name__ == "__main__":
    main()
