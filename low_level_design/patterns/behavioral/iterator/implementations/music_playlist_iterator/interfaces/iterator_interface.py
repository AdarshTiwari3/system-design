"""iterator interface implementation"""

from abc import ABC, abstractmethod

class IteratorInterface(ABC):

    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_previous(self) -> bool:
        pass

    @abstractmethod
    def previous(self):
        pass

    @abstractmethod
    def current(self):
        pass