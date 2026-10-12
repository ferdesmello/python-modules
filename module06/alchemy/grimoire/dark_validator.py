from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    found = any(item.lower() in ingredients.lower() for item in allowed)
    status = "VALID" if found else "INVALID"
    return f"({ingredients} {status})"
