"""Refined Abstraction subclass of Netbanking payment type"""

from methods.payment import Payment

class NetbankingPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"paying through netbanking system...")
        self._gateway.process_payment(amount)
