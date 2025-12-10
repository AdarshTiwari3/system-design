"""Log Appender Interface- An Appender receives a formatted LogMessage and writes it somewhere — console, file, database, network, etc."""
from abc import ABC, abstractmethod
from log_message import LogMessage
from strategies.log_formatter_strategy import LogFormatterStrategy
from strategies.text_formatter_strategy import TextFormatterStrategy

class LogAppender(ABC):
    def __init__(self, formatter: LogFormatterStrategy | None =None):
        self.formatter= formatter or TextFormatterStrategy()

    @abstractmethod
    def append(self, log_message: LogMessage):
        pass

    @abstractmethod
    def close(self):
        # Nothing to close for console
        pass

    @abstractmethod
    def get_formatter(self) -> LogFormatterStrategy:
        pass

    @abstractmethod
    def set_formatter(self, formatter: LogFormatterStrategy) -> None:
        pass