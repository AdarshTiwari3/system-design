
"""
ThreadPoolExecutor = A manager that keeps a pool of worker threads and gives them tasks to run in the background.
"""

from concurrent.futures import ThreadPoolExecutor
from typing import List
import sys

from core.log_message import LogMessage
from appenders.log_appender_interface import LogAppender  

class AsyncLogProcessor:
    """
    Very simple async log processor:
    - Uses a single background thread.
    - Logger calls process(...), which submits work to the executor.
    - The background thread calls appender.append(log_message).
    """

    def __init__(self) -> None:
        # Single worker thread is enough for logging in most cases
        self._executor = ThreadPoolExecutor(
            max_workers=1,
            thread_name_prefix='AsyncLogProcessor'
        )
        self._stopped = False

    def process(self, log_message: LogMessage, appenders: List[LogAppender]) -> None:
        
        if self._stopped:
            print("AsyncLogProcessor is stopped. Cannot process log message.", file=sys.stderr)
            return

        def task() -> None:
            for appender in appenders:
                try:
                    appender.append(log_message)
                except Exception as e:
                    # Logging errors should not crash the main app
                    print(f"Failed to append log asynchronously: {e}", file=sys.stderr)

        self._executor.submit(task)

    def stop(self) -> None:
        """
        Stop accepting new tasks and shut down the background thread.
        Call this once when your application is shutting down.
        """
        self._stopped = True
        self._executor.shutdown(wait=True)
