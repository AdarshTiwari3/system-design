"""IdleState implementation"""

from states.atm_state import ATMState
from states.card_inserted_state import CardInsertedState

class IdleState(ATMState):
    # yet to be implemented
    def insert_card(self, atm, card):
        atm.card = card
        print("💳 Card inserted")
        atm.set_state(CardInsertedState())

    def enter_pin(self, atm, pin):
        raise Exception("Insert card first")

    def select_transaction(self, atm, txn_type, amount=None):
        raise Exception("Insert card first")

    def process_transaction(self, atm):
        raise Exception("No transaction to process")

    def remove_card(self, atm):
        raise Exception("No card to remove")