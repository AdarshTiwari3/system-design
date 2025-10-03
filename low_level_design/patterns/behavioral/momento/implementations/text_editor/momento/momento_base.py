"""Momento base class implementation(Interface)"""

from abc import ABC, abstractmethod

class MomentoBase(ABC):
    @abstractmethod
    def get_saved_content(self) -> str:
        pass