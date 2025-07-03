# single instance of a class is created immediately when the class is loaded
# Create the Singleton instance immediately when the program (or module) starts — not when it's first needed.
from typing_extensions import Self

class EagerSingleton:
    _instance = None  # Internal singleton instance

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False  # Prevent multiple inits
        return cls._instance

    def __init__(self):
        if not self._initialized:
            print("Initializing EagerSingleton")
            # Put any one-time init logic here
            self._initialized = True

    @classmethod
    def get_instance(cls):
        return cls._instance


# Eagerly create the instance at module load
EagerSingleton._instance = EagerSingleton()


def run_eager_singleton():
    obj1 = EagerSingleton.get_instance()
    obj2 = EagerSingleton.get_instance()

    print(obj1 is obj2)  # Should print: True
    print(obj1)
    print(obj2)
