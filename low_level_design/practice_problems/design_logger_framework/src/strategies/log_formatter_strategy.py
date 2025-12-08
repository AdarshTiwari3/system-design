"""Log Formatter interface- How a log message is represented that's why strategy is used here"""

from abc import ABC, abstractmethod
from log_message import LogMessage
class LogFormatterStrategy(ABC):
    @abstractmethod
    def format(self, log_message: LogMessage) -> str:
        pass