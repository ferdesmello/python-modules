import sys

def inv_max_item(inv_dict: dict[str, int]) -> tuple[str, int] | None:
    if not inv_dict:
        return None

    max_item = None
    max_quantity = -1
    for item, quantity in inv_dict.items():
        if quantity > max_quantity:
            max_quantity = quantity
            max_item = item

    return max_item, max_quantity


def inv_min_item(inv_dict: dict[str, int]) -> tuple[str, int] | None:
    if not inv_dict:
        return None

    min_item = None
    min_quantity = 1000000
    for item, quantity in inv_dict.items():
        if quantity < min_quantity:
            min_quantity = quantity
            min_item = item

    return min_item, min_quantity


def load_items() -> dict[str, int]:
    inv_dict: dict[str, int] = {}

    if len(sys.argv) > 1:
        for arg in (sys.argv[1:]):
            key_value_pair = arg.split(":")
            if len(key_value_pair) != 2:
                print(f"Error invalid parameter '{arg}'")
                continue
            if key_value_pair[0] in inv_dict:
                print(f"Redundant item "
                      f"'{key_value_pair[0]}' - discarding")
                continue
            else:
                try:
                    inv_dict[key_value_pair[0]] = int(key_value_pair[1])
                except ValueError:
                    print(f"Quantity error for '{key_value_pair[0]}': "
                            f"invalid literal for int() with base 10: "
                            f"'{key_value_pair[1]}' for argument '{arg}'")
    return inv_dict


def print_inventory(inv_dict: dict[str, int]) -> None:
    if inv_dict:
        print(f"Got inventory: {inv_dict}")
        print(f"Item list: {list(inv_dict.keys())}")
        print(f"Total quantity of the {len(inv_dict)} "
              f"items: {sum(inv_dict.values())}")

        for item, quantity in inv_dict.items():
            print(f"Item: {item} represents "
                  f"{round(quantity / sum(inv_dict.values()) * 100, 1)}%")

        max_item, max_quantity = inv_max_item(inv_dict)
        print(f"Item most abundant: {max_item} with quantity {max_quantity}")

        min_item, min_quantity = inv_min_item(inv_dict)
        print(f"Item least abundant: {min_item} with quantity {min_quantity}")

    else:
        print("Error printing inventory: No items to display.")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inv_dict = load_items()
    print_inventory(inv_dict)
    if inv_dict:
        inv_dict.update({"magic_item": 1})
        print(f"Updated inventory: {inv_dict}")


if __name__ == "__main__":
    main()
