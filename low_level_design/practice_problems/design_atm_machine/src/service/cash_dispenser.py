"""Cash Dispenser of ATM which will handle the NoteDispenser of Denomination using CoR Pattern"""

from threading import Lock
from service.note_dispenser import NoteDispenser
from exceptions.domain_exception import InvalidAmountError
from service.dispense_chain import DispenseChain

class CashDispenser:
    def __init__(self):
        self._lock=Lock()

        # Create or Load cassettes (high -> low denomination)
        note_2000=NoteDispenser(2000, 15)
        note_500=NoteDispenser(500, 30)
        note_100=NoteDispenser(100, 40)
        
        # Build CoR chain
        note_2000.set_next(note_500)
        note_500.set_next(note_100)

        self._chain: DispenseChain =note_2000 # CoR Chain

    def dispense(self, amount: int):
        if amount <=0:
            raise InvalidAmountError("Invaild Cash Amount")
        

        with self._lock:
            if not self._chain.can_dispense(amount):
                raise InvalidAmountError("Cannot dispense requested amount")
            
            print(f"💵 Dispensing total amount: ₹{amount}")

            self._chain.dispense(amount)
