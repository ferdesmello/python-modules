#!/usr/bin/env python3
import alchemy.grimoire.light_spellbook as light


def main() -> None:
    print("== Kaboom 0 ==")
    print("Using grimoire module directly")
    print(f"Testing record light spell: "
          f"{light.light_spell_record('Fantasy', 'Earth, wind and fire')}")


if __name__ == "__main__":
    main()
