"""dispense state concrete class implementation"""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context.vending_machine import VendingMachine
from states.state import State

import time 

class DispenseState(State):
    """State responsible for dispensing the item after payment is complete."""

    def select_item(self, context: VendingMachine, item_code: str) -> None:
        print("\nItem is already selected")

    def pay_the_amount(self, context: VendingMachine, amount: float) -> None:
        print(f"\nPayment already done")

    def dispense_item(self, context: VendingMachine) -> None:
        item_code = context._selected_item
        context.reduce_stock(item_code)

        print(f"[Machine] Dispensed {context._inventory[item_code]['name']}.")
        print(f"\n✅Item- {context.get_selected_item()} dispensed successfully")
        print("[Machine] Returning to initial state.")


        context.reset_state()