#using singleton double checked lock pattern here

import threading
import time

class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._log_lock = threading.Lock()
            self._log_file = open("low_level_design/patterns/creational/singleton/practice_questions/logger_design/app.log", "a")  # Append mode
            self._initialized = True
            print("Logger initialized")

    def log(self, message: str):
        with self._log_lock:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            self._log_file.write(f"[{timestamp}] {message}\n")
            self._log_file.flush()

    def close(self):
        with self._log_lock:
            self._log_file.close()
            print("Logger closed.")

# --- Example usage with threads ---
def thread_task(thread_id):
    logger = Logger()
    logger.log(f"Thread {thread_id} has started logging.")

def run_logger_example():
    threads = []
    for i in range(5):
        t = threading.Thread(target=thread_task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        # print("thread=",t)
        t.join()

    logger = Logger()
    logger.log("All threads finished.")
    logger.close()

run_logger_example()
