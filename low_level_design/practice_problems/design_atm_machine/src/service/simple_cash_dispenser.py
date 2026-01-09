"""
CashDispenser- 
- Represent the physical cash unit
- Track available cash
- Prevent over-dispensing

"""
from threading import Lock
from exceptions.domain_exception import InvalidAmountError

class SimpleCashDispenser:
    def __init__(self, initial_cash: int):
        if initial_cash < 0:
            raise ValueError("Initial cash cannot be negative")

        self._available_cash=initial_cash
        self._lock=Lock()

    def dispense(self, amount: int):
        if amount < 0:
            raise InvalidAmountError("Invalid cash amount")
        
        with self._lock:
            if amount > self._available_cash:
                raise InvalidAmountError("ATM has insufficient cash")
            
            self._available_cash -= amount

        print(f"💵 Dispensed cash: {amount}")

    def get_available_cash(self) -> int:
        with self._lock:
            return self._available_cash

        



    