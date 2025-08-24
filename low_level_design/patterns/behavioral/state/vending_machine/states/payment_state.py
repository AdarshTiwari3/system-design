"""payment state concrete class implementation"""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context.vending_machine import VendingMachine
from states.state import State

from states.dispense_state import DispenseState
import time 

class PaymentState(State):
    """State after an item has been selected and payment has been made,
    waiting for the item to be dispensed.
    """
    def select_item(self, context: VendingMachine, item_code: str) -> None:
        print("\nItem is already selected")

    def pay_the_amount(self, context: VendingMachine, amount: float) -> None:
        print("\nPayment already completed. Please wait for dispensing.")

    def dispense_item(self, context: VendingMachine) -> None:
        print(f"\nDispensing the item- {context.get_selected_item()}...")
        "change the state to dispense state"
        time.sleep(2)
        context.set_state(DispenseState())
        context.dispense_item() #this is required because once payment state is called from the client as machine.dispense_item(), it calls the paymentState.dispense_item() not Dispense state's method
        
        
       

        

