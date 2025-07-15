""" XML provider interface"""

from abc import ABC, abstractmethod
class XMLDataProvider(ABC):
    @abstractmethod
    def get_data(self) -> str:
        pass