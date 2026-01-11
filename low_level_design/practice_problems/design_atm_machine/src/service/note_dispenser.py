"""
NoteDispenser represents a single ATM cash cassette
responsible for dispensing one currency denomination.
"""
from service.dispense_chain import DispenseChain
from typing import Optional
from threading import Lock


class NoteDispenser(DispenseChain):
    def __init__(self, denomination: int, note_count: int):
        self._denomination = denomination          # Value of each note (e.g. Rs 2000)
        self._note_count = note_count               # Number of available notes
        self._next: Optional[DispenseChain] = None  # Next handler in CoR
        self._lock = Lock()

    def set_next(self, next_chain: DispenseChain):
        # Link next denomination handler
        self._next = next_chain

    def can_dispense(self, amount: int) -> bool:
        # Base cases
        if amount == 0:
            return True
        if amount < 0:
            return False

        with self._lock:
            requested_notes = amount // self._denomination
            usable_notes = min(requested_notes, self._note_count)
            # Remaining amount to be handled by the next dispenser
            remaining_amount = amount - (usable_notes * self._denomination)

        if remaining_amount == 0:
            return True

        # Forward remaining amount to next handler in the chain
        return self._next.can_dispense(remaining_amount) if self._next else False

    def dispense(self, amount: int):
        with self._lock:
            notes = min(amount // self._denomination, self._note_count)
            remaining_amount = amount - (notes * self._denomination)

            if notes > 0:
                print(f"Dispensing {notes} x ₹{self._denomination} notes")
                self._note_count -= notes

        # Pass remaining amount to next dispenser if needed
        if remaining_amount > 0:
            if self._next:
                self._next.dispense(remaining_amount)
            else:
                raise Exception("Cannot dispense remaining amount")
