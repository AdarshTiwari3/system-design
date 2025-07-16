"""Implementor interface of Bridge Design Pattern"""
from abc import ABC, abstractmethod

class Gateways(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass