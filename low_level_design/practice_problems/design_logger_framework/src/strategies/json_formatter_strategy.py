"""Log Formatter strategy- JsonFormatter"""

from strategies.log_formatter_strategy import LogFormatterStrategy
from log_message import LogMessage
import json

class JsonFormatterStrategy(LogFormatterStrategy):
    def format(self, log_message: LogMessage) -> str:
        return json.dumps({
            "timestamp": log_message.get_timestamp().isoformat(),
            "level": log_message.get_log_level().name,
            "logger": log_message.get_logger_name(),
            "thread": log_message.get_thread_name(),
            "message": log_message.get_message()
        })
