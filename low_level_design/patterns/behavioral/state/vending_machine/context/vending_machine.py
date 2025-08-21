"""Implementation of Context - Vending Machine using State Pattern"""

from states.state import State
from states.initial_state import InitialState
from typing import Dict, Any


class VendingMachine:
    def __init__(self, inventory: Dict[str, Dict[str, Any]]) -> None:
        """
        A vending machine will have:
        1. current_state: current operational state
        2. inserted_amount: total money inserted by user
        3. selected_item: currently chosen item
        4. inventory: available items with price & stock
        """
        self._current_state: State = InitialState()
        self._inserted_amount: float = 0.0
        self._selected_item: str = ""
        self._inventory: Dict[str, Dict[str, Any]] = inventory

    def set_state(self, new_state: State) -> None:
        """Update current state of vending machine."""
        self._current_state = new_state

    def set_selected_item(self, item_code: str) -> None:
        """Store selected item inside context."""
        self._selected_item = item_code

    def add_amount(self, amount: float) -> None:
        """Update inserted amount after user payment."""
        self._inserted_amount += amount

    def get_selected_item(self) -> str:
        return self._selected_item

    def get_inserted_amount(self) -> float:
        return self._inserted_amount

    def get_inventory(self) -> dict:
        return self._inventory

    # ---- Delegated actions to state of vending machine ----
    def select_item(self, item_code: str) -> None:
        self._current_state.select_item(self, item_code)

    def pay_the_amount(self, amount: float) -> None:
        self._current_state.pay_the_amount(self, amount) #here self will be context which is vending machine only

    def dispense_item(self) -> None:
        self._current_state.dispense_item(self)

    def reduce_stock(self, item_code: str) -> None:
        if self._inventory[item_code]["stock"] > 0:
            self._inventory[item_code]["stock"] -= 1
        else:
            print(f"[Machine] Item {item_code} is out of stock!")

    def get_item_price(self, item_code: str) -> float:
        """Return the price of a given item if it exists, else raise error."""
        if item_code not in self._inventory:
            raise ValueError(f"Item {item_code} not found in inventory")
        return self._inventory[item_code]["price"]
    
    def reset_state(self):
        self._current_state=InitialState()
        self._selected_item=""
        self._inserted_amount=0.0
