""" 
A ConsoleAppender is something that prints logs on the screen (your terminal / console).
or ConsoleAppender = write logs to the screen.
Example: 

[INFO] Payment started

"""
import threading
from appenders.log_appender_interface import LogAppender
from strategies.log_formatter_strategy import LogFormatterStrategy
from core.log_message import LogMessage
class ConsoleAppender(LogAppender):
    _lock = threading.Lock() 

    def append(self, log_message: LogMessage):
        formatted = self.formatter.format(log_message)
        with ConsoleAppender._lock:
            print(formatted)
    def close(self):
        pass

    def set_formatter(self, formatter: LogFormatterStrategy):
        self.formatter=formatter

    def get_formatter(self) -> LogFormatterStrategy:
        return self.formatter