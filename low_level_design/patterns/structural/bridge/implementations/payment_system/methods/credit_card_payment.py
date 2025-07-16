"""Refined Abstraction subclass of Credit card payment type"""

from methods.payment import Payment

class CreditCardPayment(Payment):
    def pay(self, amount: float) -> None:
            print(f"paying through credit card")
            self._gateway.process_payment(amount)