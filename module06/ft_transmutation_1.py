#!/usr/bin/env python3
import alchemy.transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print("Testing lead to gold: "
          f"{alchemy.transmutation.lead_to_gold()}")


if __name__ == "__main__":
    main()
