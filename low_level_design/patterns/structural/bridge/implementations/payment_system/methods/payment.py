"""Abstraction Implementation of Bridge Pattern"""
"""why this because payment uses gateway not gatway uses payment"""

from abc import ABC, abstractmethod
from gateways.gateways import Gateways
class Payment(ABC):
    def __init__(self, gateway: Gateways) -> None:
        self._gateway=gateway # Bridge (composition)
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass