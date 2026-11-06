from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability
from typing import cast


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, Creature))

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.creature_name}' "
                "for this normal strategy"
            )
        return (creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, TransformCapability))

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.creature_name}' "
                "for this aggressive strategy"
            )
        return (cast(TransformCapability, creature).transform() + "\n"
                + creature.attack() + "\n"
                + cast(TransformCapability, creature).revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, HealCapability))

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.creature_name}' "
                f"for this defensive strategy"
            )
        return (creature.attack() + "\n"
                + cast(HealCapability, creature).heal())
