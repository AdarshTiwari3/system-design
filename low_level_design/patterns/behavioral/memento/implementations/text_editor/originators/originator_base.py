"""Originator Interface Class"""

from abc import ABC , abstractmethod
from memento.memento_base import MementoBase

class OriginatorInterface(ABC):

    @abstractmethod
    def write(self, text: str):
        """write text to editor"""
        pass

    @abstractmethod
    def save(self) -> MementoBase:
        """save current state"""
        pass

    @abstractmethod
    def restore(self, memento : MementoBase) -> None:
        """restores the state"""
        pass