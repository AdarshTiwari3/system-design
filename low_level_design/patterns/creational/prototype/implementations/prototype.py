""" Prototype Interface class and its concreate classes will have the clone method which will provide the feature of cloning"""
from abc import ABC, abstractmethod
from typing_extensions import Self
class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Self:
        pass