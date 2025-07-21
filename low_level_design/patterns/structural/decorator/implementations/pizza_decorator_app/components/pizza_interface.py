"""Implmentation of Pizza Interface"""

from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass