"""subclass implementation of template method- credit card checkout"""
from checkout.base_checkout import CheckoutProcess

class CreditCardCheckout(CheckoutProcess):
    TRANSACTION_FEE = 25.0  

    def make_payment(self, order: dict):
        total: float = order.get('total', 0.0)
        final_amount = total + self.TRANSACTION_FEE
        print(f"\n[Credit Card] Processing payment. Amount: {total} INR + "
              f"Fee: {self.TRANSACTION_FEE},Total = {final_amount} INR")
