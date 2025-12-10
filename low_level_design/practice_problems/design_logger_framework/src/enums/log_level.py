"""Log Level implementation for common logging levels."""

from enum import IntEnum


class LogLevel(IntEnum):
    """Uses 10-based increments to easily accommodate additional log levels."""
    
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    FATAL = 50

    def is_greater_or_equal(self, other: 'LogLevel') -> bool:
        """The “greater than or equal” check ensures that only important-enough log messages (based on configured log level) are written. Lower-priority messages are ignored."""
        
        return self.value >= other.value