from elements import create_fire
from alchemy.elements import create_air
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
    text: str = ("Recipe transmuting Lead to Gold: brew "
                 + f"'{create_air()}' and "
                 + f"'{strength_potion()}' mixed with "
                 + f"'{create_fire()}'")
    return text
