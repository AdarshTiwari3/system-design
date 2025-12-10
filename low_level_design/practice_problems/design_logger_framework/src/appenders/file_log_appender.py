"""
A FileAppender is something that writes logs into a file on your computer
or FileAppender = save logs to a file.
Example:
app.log
error.log
server.log

"""
import threading
from appenders.log_appender_interface import LogAppender
from strategies.log_formatter_strategy import LogFormatterStrategy
from log_message import LogMessage

class FileAppender(LogAppender):
    def __init__(self,file_path:str, formatter: LogFormatterStrategy | None = None):
        """
        file_path: path of the log file where logs will be written.
        formatter: optional formatter strategy (Text/JSON). Defaults to TextFormatter.
        """

        super().__init__(formatter)
        self.file_path = file_path
        self._lock = threading.Lock()

        self._file = open(self.file_path, "a", encoding="utf-8")

    def append(self, log_message: LogMessage):
        """Write formatted log message into the file safely."""
        formatted = self.formatter.format(log_message)

        with self._lock:
            self._file.write(formatted+'\n')
            self._file.flush()  # ensures logs are written even if system crashes

    def close(self):
        """Close the open file"""
        with self._lock:
            if not self._file.closed:
                self._file.close()

    def get_formatter(self) -> LogFormatterStrategy:
        return self.formatter
    
    def set_formatter(self, formatter: LogFormatterStrategy) -> None:
        self.formatter=formatter


        
