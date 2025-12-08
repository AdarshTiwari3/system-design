"""Log Level implementation for common logging levels."""

from enum import Enum, IntEnum


class LogLevel(IntEnum):
    """Uses 10-based increments to easily accommodate additional log levels."""
    
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    FATAL = 50

    def is_greater_or_equal(self, other: 'LogLevel') -> bool:
        return self.value >= other.value