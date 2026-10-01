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


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            accepted: bool = False

            for process in self._processors:
                if process.validate(item):
                    process.ingest(item)
                    accepted = True
                    break

            if not accepted:
                print(f"DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data\n")
        else:
            for process in self._processors:
                process_name: str = type(process).__name__
                name: str
                if process_name == "NumericProcessor":
                    name = "Numeric Processor"
                elif process_name == "TextProcessor":
                    name = "Text Processor"
                elif process_name == "LogProcessor":
                    name = "Log Processor"
                print(f"{name}: "
                      f"total {process._index} items processed, "
                      f"remaining {len(process._values)} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    data_stream = DataStream()

    data_stream.print_processors_stats()

    print("Registering Numeric Processor\n")
    numeric = NumericProcessor()

    data: list[typing.Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [{
            'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO', 'log_message': 'User wil is connected'
                }],
        42,
        ['Hi', 'five']
        ]
    print(f"Send first batch of data on stream: {data}")

    data_stream.register_processor(numeric)
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    text = TextProcessor()
    data_stream.register_processor(text)
    log = LogProcessor()
    data_stream.register_processor(log)

    print("Send the same batch again")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    pop_num: int = 3
    pop_text: int = 2
    pop_log: int = 1
    pop_dict = {
        "NumericProcessor": pop_num,
        "TextProcessor": pop_text,
        "LogProcessor": pop_log,
    }
    print(f"\nConsume some elements from the data processors: "
          f"Numeric {pop_num}, Text {pop_text}, Log {pop_log}")
    for process in data_stream._processors:
        process_name: str = type(process).__name__
        executions: int = pop_dict.get(process_name, 0)
        for _ in range(executions):
            try:
                process.output()
            except IndexError:
                break

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
