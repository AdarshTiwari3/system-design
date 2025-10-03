"""Originator Interface Class"""

from abc import ABC , abstractmethod
from momento.momento_base import MomentoBase

class OriginatorInterface(ABC):

    @abstractmethod
    def write(self, text: str):
        """write text to editor"""
        pass

    @abstractmethod
    def save(self) -> MomentoBase:
        """save current state"""
        pass

    @abstractmethod
    def restore(self, momento : MomentoBase) -> None:
        """restores the state"""
        pass