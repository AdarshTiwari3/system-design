"""State Interface Implementation"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context.vending_machine import VendingMachine #delays the type hint at run time to avoid circular import error

class State(ABC):
    """Majorly here we will perform 3 operations-
    1. select_item- to choose item from vending machine
    2. pay_the_amount- to do the payment
    3. dispense_item- to dispense the item
    """

    @abstractmethod
    def select_item(self, context: VendingMachine, item_code: str) -> None: #context is there because states must control the behavior and transitions of the vending machine.
        """Select an item from the vending machine."""
        pass

    @abstractmethod
    def pay_the_amount(self, context: VendingMachine, amount: float) -> None:
        """Handle payment for the selected item."""
        pass

    @abstractmethod
    def dispense_item(self, context: VendingMachine) -> None:
        """Dispense the selected item."""
        pass