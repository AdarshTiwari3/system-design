"""ATM State Interface"""

from abc import ABC, abstractmethod
from entities.card import Card
from enums.txn_type import TransactionType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.atm import ATM

    
class ATMState(ABC):
    @abstractmethod
    def insert_card(self, atm: "ATM" , card: Card): #here ATM is context
        pass

    @abstractmethod
    def enter_pin(self, atm: "ATM", pin: str):
        pass

    @abstractmethod
    def select_transaction(self, atm: "ATM", txn_type: TransactionType, amount: int | None=None):
        pass

    @abstractmethod
    def process_transaction(self, atm: "ATM"):
        pass

    @abstractmethod
    def remove_card(self, atm: "ATM"):
        pass 