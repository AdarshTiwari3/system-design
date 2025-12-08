from strategies.log_formatter_strategy import LogFormatterStrategy
from log_message import LogMessage

class TextFormatterStrategy(LogFormatterStrategy):
    def format(self, log_message: LogMessage) -> str:
        return (
            f"[{log_message.get_timestamp()}] "
            f"[{log_message.get_log_level().name}] "
            f"[{log_message.get_logger_name()}] "
            f"[{log_message.get_thread_name()}] "
            f"{log_message.get_message()}"
        )