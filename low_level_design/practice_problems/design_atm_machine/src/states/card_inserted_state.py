"""CardInsertedState"""

from states.atm_state import ATMState


from exceptions.auth_exception import InvalidPINError
from states.authenticated_state import AuthenticatedState


class CardInsertedState(ATMState):
    #yet to be implemented
    def insert_card(self, atm, card):
        raise Exception("Card already inserted")
    

    def enter_pin(self, atm, pin):
        try:
            if atm.card.is_expired():
                raise Exception("Card expired")

            atm.validate_pin(atm.get_card_number(), pin)

            print("✅ PIN validated successfully")
            atm.set_state(AuthenticatedState())



        except InvalidPINError as e:
            print(str(e))
            self.remove_card(atm)
    
    def select_transaction(self, atm, txn_type, amount = None):
         raise Exception("Authenticate first")
    
    def process_transaction(self, atm):
        raise Exception("Authenticate first")
    
    def remove_card(self, atm):
        atm.reset()
        print("💳 Card removed")
