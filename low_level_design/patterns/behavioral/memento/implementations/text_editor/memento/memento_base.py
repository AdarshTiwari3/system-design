"""Momento base class implementation(Interface)"""

from abc import ABC, abstractmethod

class MementoBase(ABC):
    @abstractmethod
    def get_saved_content(self) -> str:
        pass