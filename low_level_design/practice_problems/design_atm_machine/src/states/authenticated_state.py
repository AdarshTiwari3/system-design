"""AuthenticatedState Implementation"""

from states.atm_state import ATMState
from enums.txn_type import TransactionType
from states.processing_state import ProcessingState


class AuthenticatedState(ATMState):
    #yet to be implemented
    def insert_card(self, atm, card):
        raise Exception("Card already inserted")

    def enter_pin(self, atm, pin: str):
        raise Exception("Already authenticated")
    def select_transaction(self, atm, txn_type, amount = None):
        if txn_type in (TransactionType.WITHDRAW_CASH, TransactionType.DEPOSIT_CASH):
            if amount is None or amount <= 0:
                raise Exception("Valid amount required")
            
        if txn_type == TransactionType.CHECK_BALANCE:
            amount = None

        atm.txn_type = txn_type
        atm.amount = amount

        print(f"➡️ Operation selected: {txn_type.value}")

        atm.set_state(ProcessingState())


        

    def process_transaction(self, atm):
        raise Exception("Select transaction first")

    def remove_card(self, atm):
        atm.reset()
        print("💳 Card removed")
