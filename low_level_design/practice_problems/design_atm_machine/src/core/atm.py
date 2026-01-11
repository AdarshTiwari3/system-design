from states.atm_state import ATMState
from entities.card import Card
from enums.txn_type import TransactionType
from service.auth_service import AuthService
from service.bank_service import BankService
from service.cash_dispenser import CashDispenser

class ATM:
    # def __init__(self, auth_service: AuthService, bank_service: BankService, cash_dispenser: SimpleCashDispenser): # if we go for simple dispenser
    def __init__(self, auth_service: AuthService, bank_service: BankService, cash_dispenser: CashDispenser):
      
        self.current_state=None
        self.card: Card | None=None
        self.bank_service=bank_service
        self.auth_service = auth_service 
        self.cash_dispenser = cash_dispenser

        #per session data
        self.txn_type: TransactionType | None = None
        self.amount: int | None = None

        self.move_to_idle()


    def set_state(self, state: ATMState):
        self.current_state=state

    def move_to_idle(self):
        from states.idle_state import IdleState
        self.current_state = IdleState()


    def reset(self):
        self.card=None
        self.txn_type = None
        self.amount = None
        self.move_to_idle()

    def insert_card(self, card: Card):
        self.current_state.insert_card(self, card)

    def enter_pin(self, pin: str):
        self.current_state.enter_pin(self, pin)

    def select_transaction(self, txn_type: TransactionType, amount : int | None = None):
        self.current_state.select_transaction(self, txn_type, amount)

    def remove_card(self):
        self.current_state.remove_card(self)

    def process_transaction(self):
        self.current_state.process_transaction(self)


    # Facade methods

    def validate_pin(self, card_number, pin):
        self.auth_service.validate_pin(card_number, pin)

    def get_card_number(self):
        if not self.card:
            raise Exception("No card inserted")
        return self.card.card_number