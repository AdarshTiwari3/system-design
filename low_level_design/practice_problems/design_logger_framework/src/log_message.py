"""LogMessage- Represents a single log entry"""
from datetime import datetime
from enums.log_level import LogLevel
import threading

class LogMessage:
    def __init__(self, level: LogLevel, message: str, logger_name: str):
        self.timestamp=datetime.now()
        self.level=level
        self.message=message
        self.logger_name=logger_name
        self.thread_name=threading.current_thread().name

    def get_message(self) -> str:
        return self.message
    
    def get_timestamp(self) -> datetime:
        return self.timestamp
    
    def get_log_level(self) -> LogLevel:
        return self.level
    
    def get_logger_name(self) -> str:
        return self.logger_name
    
    def get_thread_name(self) -> str:
        return self.thread_name