"""Auth Service implementation"""
import hashlib
from exceptions.auth_exception import InvalidPINError
from threading import Lock

class AuthService:
    def __init__(self):
        self._pin_store={} #stores hashed pin
        self._lock=Lock()

    def register_pin(self, account_number: str, pin: str):
        with self._lock:
            self._pin_store[account_number]=self._hash(pin)

    def validate_pin(self, account_number:str, entered_pin: str) -> None:
        with self._lock:
            stored_hash=self._pin_store.get(account_number)

        if not stored_hash or stored_hash != self._hash(entered_pin):
            raise InvalidPINError("Invalid PIN")
        
        

    def _hash(self, pin: str):
        return hashlib.sha256(pin.encode()).hexdigest() # hexdigest() converts the binary output of a hash function into a human-readable hexadecimal string.

