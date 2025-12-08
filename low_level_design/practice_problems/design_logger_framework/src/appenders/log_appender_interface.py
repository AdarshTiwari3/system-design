"""Log Appender Interface"""
from abc import ABC, abstractmethod
from log_message import LogMessage
class LogAppender(ABC):
    @abstractmethod
    def append(self, log_message: LogMessage):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def get_formatter(self):
        pass

    @abstractmethod
    def set_formatter(self, formatter):
        pass