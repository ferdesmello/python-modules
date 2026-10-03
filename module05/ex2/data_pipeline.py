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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        lines = [f"{value}" for index, value in data]
        print("CSV Output:\n" + ", ".join(lines))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = {f"item_{index}": value for index, value in data}
        print(f"JSON Output:\n{items}")


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
        print("\n== DataStream statistics ==")
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for process in self._processors:
            extracted_data: list[tuple[int, str]] = []

            number: int = nb
            process_length: int = len(process._values)
            if process_length < nb:
                number = process_length
            else:
                number = nb

            for _ in range(number):
                item = process.output()
                extracted_data.append(item)

            if extracted_data:
                plugin.process_output(extracted_data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...")
    data_stream = DataStream()

    data_stream.print_processors_stats()

    print("Registering Processors\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    data_stream.register_processor(numeric)
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    data1: list[typing.Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [{
            'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'
            },
            {
            'log_level': 'INFO',
            'log_message': 'User wil is connected'
            }],
        42,
        ['Hi', 'five']
        ]
    print(f"Send first batch of data on stream: {data1}")
    data_stream.process_stream(data1)
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    data_stream.output_pipeline(3, csv_plugin)

    data_stream.print_processors_stats()

    data2: list[typing.Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{
            'log_level': 'ERROR',
            'log_message': '500 server crash'
            },
            {
            'log_level': 'NOTICE',
            'log_message': 'Certificate expires in 10 days'
        }],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {data2}")
    data_stream.process_stream(data2)
    data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    data_stream.output_pipeline(5, json_plugin)

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
