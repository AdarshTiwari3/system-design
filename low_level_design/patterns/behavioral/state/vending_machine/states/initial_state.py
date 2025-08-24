"""Initial state concrete class implementation"""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context.vending_machine import VendingMachine
from states.state import State
from states.item_selected_state import ItemSelectedState


class InitialState(State):
    """State awaiting item to be selected"""
    def select_item(self, context:VendingMachine, item_code: str) -> None:
        if item_code not in context._inventory:
            print("\nInvaild item number, please enter correct item number")
            return
        elif context._inventory[item_code]["stock"] <= 0:
            print("\nItem out of stock")
            return 

        #select the amount
        context.set_selected_item(item_code)
        print(f"Item {item_code} selected from the Machine")
        context.set_state(ItemSelectedState())
            
    
    def pay_the_amount(self, context:VendingMachine, amount: float) -> None:
        print(f"\nPlease select an item first before payment")
    
    def dispense_item(self, context:VendingMachine) -> None:
        print(f"\nNo item selected to dispense")