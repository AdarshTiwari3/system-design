"""Payment Processing State"""

from states.atm_state import ATMState
from states.idle_state import IdleState
from enums.txn_type import TransactionType
from typing import TYPE_CHECKING
from exceptions.domain_exception import (InsufficientBalanceError, InvalidAmountError, AccountNotFoundError)

if TYPE_CHECKING:
    from core.atm import ATM

class ProcessingState(ATMState):
    """ Transaction is processing """

    def insert_card(self, atm: "ATM", card):
        raise Exception("Transaction in progress")

    def enter_pin(self, atm: "ATM", pin: str):
        raise Exception("Transaction in progress")

    def select_transaction(self, atm: "ATM", txn_type, amount=None):
        raise Exception("Transaction in progress")

    def process_transaction(self, atm: "ATM"):
        card_number=atm.get_card_number()

        try:
            if atm.txn_type == TransactionType.CHECK_BALANCE:
                balance=atm.bank_service.get_balance(card_number)
                print(f"💰 Current Balance: {balance}")

            elif atm.txn_type == TransactionType.WITHDRAW_CASH:
                atm.bank_service.withdraw(card_number,atm.amount)
                
                atm.cash_dispenser.dispense(atm.amount)

                print(f"💸 Withdrawn: {atm.amount}")

            elif atm.txn_type == TransactionType.DEPOSITE_CASH:
                atm.bank_service.deposit(card_number,atm.amount)
                print(f"💵 Deposited: {atm.amount}")

            else:
                raise Exception("Unknown transaction type")

            print("✅ Transaction completed successfully")

        except (InsufficientBalanceError, InvalidAmountError, AccountNotFoundError) as e:
            print(f"❌ Transaction failed: {str(e)}")

        finally:
            # Always end session
            atm.reset()
            atm.set_state(IdleState())
            print("🔁 ATM reset to Idle state")

        

    def remove_card(self, atm: "ATM"):
        raise Exception("Cannot remove card during transaction")

    
    