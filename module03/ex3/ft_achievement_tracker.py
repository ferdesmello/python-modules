#!/usr/bin/env python3
import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    number = random.randint(5, 10)
    random_elements = random.sample(list(achievements), number)
    return set(random_elements)


def main() -> None:
    achievements = [
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Unstoppable',
        'First Steps',
        'Collector Supreme',
        'Untouchable',
        'Sharp Mind',
        'Boss Slayer'
        ]
    players_names_l: list[str] = [
        'Alice',
        'Bob',
        'Charlie',
        'Dylan',
        'Eve'
        ]
    players_sets_l: list[set[str]] = []

    print("=== Achievement Tracker System ===\n")

    for player in players_names_l:
        player_set = gen_player_achievements(achievements)
        print(f"Player {player}: {player_set}")
        players_sets_l.append(player_set)

    all_distinct = set().union(*players_sets_l)
    print(f"\nAll distinct achievements: {all_distinct}")

    common_ones = set.intersection(*players_sets_l)
    print(f"\nCommon achievements: {common_ones}\n")

    for player_name in players_names_l:
        other_players_s: list[set[str]] = []
        for other_player_name in players_names_l:
            if other_player_name != player_name:
                other_index = players_names_l.index(other_player_name)
                other_players_s.append(players_sets_l[other_index])

        index = players_names_l.index(player_name)
        player_set = players_sets_l[index]
        unique_to_player = player_set.difference(set()
                                                 .union(*other_players_s))

        print(f"Only {player_name} has: {unique_to_player}")

    print()

    for player_name in players_names_l:
        index = players_names_l.index(player_name)
        player_set = players_sets_l[index]
        missing_to_player = set(achievements).difference(player_set)

        print(f"{player_name} is missing: {missing_to_player}")


if __name__ == "__main__":
    main()
