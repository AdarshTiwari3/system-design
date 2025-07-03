#using singleton design pattern with double checked lock pattern
import threading
import sqlite3
from typing import Optional

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls) -> "DatabaseConnection":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            
            self._connection = sqlite3.connect("low_level_design/patterns/creational/singleton/practice_questions/db_connection_pool/myapp.db", check_same_thread=False)
            self._query_lock = threading.Lock()  # Lock for executing queries
            self._initialized = True
            print("Database connection created.")

    def execute_query(self, query: str, params: Optional[tuple] = None):
        with self._query_lock:
            cursor = self._connection.cursor()
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                self._connection.commit()
                return cursor.fetchall()
            finally:
                cursor.close()

    def close_connection(self):
        with self._query_lock:
            self._connection.close()
            print("Database connection closed.")


def run_db_task():
    db = DatabaseConnection()
    db.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute_query("INSERT INTO users (name) VALUES (?)", ("John Doe",))
    users = db.execute_query("SELECT * FROM users")
    print("Fetched users:", users)


def run_multithreaded_db_example():
    threads = []
    for _ in range(3):
        t = threading.Thread(target=run_db_task)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    db = DatabaseConnection()
    db.close_connection()

run_multithreaded_db_example()
