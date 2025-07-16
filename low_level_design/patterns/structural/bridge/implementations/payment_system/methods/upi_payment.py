"""Refined Abstraction subclass of UPI payment type"""


from methods.payment import Payment

class UPIPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"paying through UPI...")
        self._gateway.process_payment(amount)