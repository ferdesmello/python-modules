#!/usr/bin/env python3
import typing
import abc


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self._values: list[tuple[int, str]] = []
        self._index: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._values:
            raise IndexError("No data to output")
        return self._values.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True

        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items: list[int | float] = data if isinstance(data, list) else [data]
        for item in items:
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                self._values.append((self._index, str(item)))
                self._index += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(x, str) for x in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        items: list[str] = data if isinstance(data, list) else [data]
        for item in items:
            if isinstance(item, str):
                self._values.append((self._index, item))
                self._index += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        def is_valid_log_entry(entry: typing.Any) -> bool:
            if not isinstance(entry, dict):
                return False
            required_keys = {"log_level", "log_message"}
            return required_keys.issubset(entry.keys()) and all(
                isinstance(entry[key], str) for key in required_keys
            )

        if isinstance(data, dict):
            return all(is_valid_log_entry(v) for v in data.values())

        if isinstance(data, list) and len(data) > 0:
            return all(is_valid_log_entry(v) for v in data)

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        items: list[dict[str, str]] = []
        items = data if isinstance(data, list) else [data]

        for item in items:
            formatted_val = f"{item['log_level']}: {item['log_message']}"
            self._values.append((self._index, formatted_val))
            self._index += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    input1: int | float = 42
    input2: str = "Hello"
    input3: list[int | float] = [1, 2, 3, 4, 5.0]
    input4: list[str] = ['Hello', 'Nexus', 'World']
    input5: dict[str, str] | list[dict[str, str]] = [{
        'log_level': 'NOTICE',
        'log_message': 'Connection to server'},
        {'log_level': 'ERROR',
         'log_message': 'Unauthorized access!!'}
         ]

    print()
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f" Trying to validade input '{input1}': ", end="")
    print(numeric.validate(input1))

    print(f" Trying to validade input '{input2}': ", end="")
    print(numeric.validate(input2))

    print(f" Test invalid ingestion of string '{input2}' "
          f"without prior validation:")
    try:
        numeric.ingest(input2)
    except Exception as e:
        print(f" Got exception: {e}")

    print(" Extracting 3 values...")
    numeric.ingest(input3)
    for _ in range(3):
        pos, value = numeric.output()
        print(f" Numeric value {pos}: {value}")

    print()
    print("Testing Text Processor...")
    text = TextProcessor()
    print(f"Trying to validade input '{input1}': ", end="")
    print(text.validate(input1))

    print(f" Trying to validade input '{input2}': ", end="")
    print(text.validate(input2))

    print(f" Test invalid ingestion of number '{input1}' "
          f"without prior validation:")
    try:
        text.ingest(input1)
    except Exception as e:
        print(f" Got exception: {e}")

    print(" Extracting 2 values...")
    text.ingest(input4)
    for _ in range(2):
        pos, value = text.output()
        print(f" Text value {pos}: {value}")

    print()
    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying to validade input '{input1}': ", end="")
    print(log.validate(input1))

    print(f" Test invalid ingestion of string '{input2}' "
          f"without prior validation:")
    try:
        log.ingest(input2)
    except Exception as e:
        print(f" Got exception: {e}")

    print(f" Processing data: {input5}")
    print(f" Extracting {len(input5)} values...")
    log.ingest(input5)
    for _ in range(len(input5)):
        pos, value = log.output()
        print(f" Log entry {pos}: "
              f"{value}")


if __name__ == "__main__":
    main()
