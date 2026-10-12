from alchemy.elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    text: str = ("Healing potion brewed with "
                 + f"'{create_earth()}' and "
                 + f"'{create_air()}'")
    return text


def strength_potion() -> str:
    text: str = ("Strength potion brewed with "
                 + f"'{create_fire()}' and "
                 + f"'{create_water()}'")
    return text
