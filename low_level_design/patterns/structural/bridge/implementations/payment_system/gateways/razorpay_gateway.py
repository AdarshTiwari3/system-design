""" Concreate Implementor of Razorpay Gateway"""
from gateways.gateways import Gateways

class RazorpayGateway(Gateways):
    def process_payment(self, amount: float) -> None:
        print(f"Razorpay is processing the amount: ₹{amount:0.2f}")