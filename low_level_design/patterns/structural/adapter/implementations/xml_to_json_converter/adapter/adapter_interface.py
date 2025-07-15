""" JSON provider interface , acts as Adapter"""

from abc import ABC, abstractmethod

class JSONDataProvider(ABC):
    @abstractmethod
    def get_data(self) -> str:
        pass