""" Concreate Implementor of Stripe Gateway"""

from gateways.gateways import Gateways
 
class StripeGateway(Gateways):
    def process_payment(self, amount: float) -> None:
        print(f"Stripe is processing the amount: ₹{amount:0.2f}")