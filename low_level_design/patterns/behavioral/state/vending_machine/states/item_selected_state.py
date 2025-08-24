"""ItemSelected state concrete class implementation"""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context.vending_machine import VendingMachine  #using this to delay the type hint checks to aviod circular import
from states.state import State

from states.payment_state import PaymentState

class ItemSelectedState(State):
    """State after an item has been selected, waiting for payment."""

    def select_item(self, context: VendingMachine, item_code: str) -> None:
        print("\nItem is already selected, please proceed to payment")

    def pay_the_amount(self, context: VendingMachine, amount: float) -> None:
        item_code = context.get_selected_item()
        item_price = context.get_item_price(item_code)

        # add inserted money
        context.add_amount(amount)
        print(f"[Machine] Payment of {amount} accepted. Total inserted: {context.get_inserted_amount()}")

        if context.get_inserted_amount() < item_price:
            print(f"[Payment] Still need {item_price - context.get_inserted_amount()} more.")
            return

        # Move to payment state once enough funds are inserted
        context.set_state(PaymentState())
        
    def dispense_item(self, context: VendingMachine) -> None:
        print("\nPlease pay the amount, Item can't be dispensed without payment")
