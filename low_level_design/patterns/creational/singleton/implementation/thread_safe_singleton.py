# A thread-safe singleton ensures that only one instance of the singleton class is ever created, even when multiple threads try to access it simultaneously.
import threading
# the code is both Thread Safe Singleton and Double checked lock pattern 
class ThreadSafeSingleton:
    _instance = None  # Used for storing the singleton instance
    _lock = threading.Lock()  # Used to synchronize threads

    def __new__(cls):
        # First check without locking (improves performance in common case)
        if cls._instance is None:
            with cls._lock:
                # Double-checked locking: still None?
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        # Ensure the singleton is initialized before returning
        if cls._instance is None:
            cls()  # Triggers __new__ to create the instance
        return cls._instance

def run_thread_safe_singleton():
    obj1 = ThreadSafeSingleton.get_instance()
    obj2 = ThreadSafeSingleton.get_instance()

    print(obj1 is obj2) # True
    print(obj1)
    print(obj2)


