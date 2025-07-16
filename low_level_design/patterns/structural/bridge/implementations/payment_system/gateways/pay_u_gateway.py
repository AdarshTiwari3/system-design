""" Concreate Implementor of PayU Gateway"""

from gateways.gateways import Gateways

class PayUGateway(Gateways):
    def process_payment(self, amount: float) -> None:
        print(f"Pay U is processing the amount: ₹{amount:0.2f}")