from abc import ABC, abstractmethod
from interfaces.iterator_interface import IteratorInterface
class IterableCollectionInterface(ABC):
    @abstractmethod
    def get_iterator(self) -> IteratorInterface:
        pass