#!/usr/bin/env python3
import random


def main() -> None:

    names = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam']

    all_cap_names = [name.capitalize() for name in names]
    cap_names_only = [name for name in names if name == name.capitalize()]

    score_dict = {name: random.randint(10, 1000) for name in all_cap_names}
    average_score = sum(score_dict.values()) / len(score_dict)
    high_scores = {name: score_dict[name] for name in
                   score_dict.keys() if score_dict[name] > average_score}

    print("=== Game Data Alchemist ===\n")

    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {all_cap_names}")
    print(f"New list of capitalized names only: {cap_names_only}")

    print(f"\nScore dict: {score_dict}")
    print(f"Score average is {round(average_score, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
