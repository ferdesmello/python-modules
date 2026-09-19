#!/usr/bin/env python3
import random
import typing


def gen_event(
        names: list[str],
        actions: list[str]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(names)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
        ten_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while ten_list:
        index = random.randint(0, len(ten_list) - 1)
        item = ten_list.pop(index)
        yield item


def main() -> None:
    actions = [
        'run',
        'eat',
        'sleep',
        'grab',
        'move',
        'climb',
        'swim',
        'release',
        'jump',
        'attack',
        'defend',
        'craft',
        'build',
        'destroy',
        'explore',
        'trade',
        'talk',
        'listen',
        'watch',
        'hide',
        'seek',
        'search',
        'find'
        ]
    names = [
        'Alice',
        'Bob',
        'Charlie',
        'Dylan',
        'Edna',
        'Fiona'
        ]

    print("=== Game Data Stream Processor ===")

    stream = gen_event(names, actions)

    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    ten_items: list[tuple[str, str]] = []
    for i in range(10):
        ten_items.append(next(stream))
    print(f"Built list of 10 events: {ten_items}")

    for event in consume_event(ten_items):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_items}")


if __name__ == "__main__":
    main()
