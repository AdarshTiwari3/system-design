"""Base Element interface which defines the accept method for Visitors."""

from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass