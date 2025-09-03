"""subclass implementation of template method- UPI checkout"""
from checkout.base_checkout import CheckoutProcess

class UPICheckout(CheckoutProcess):
    TRANSACTION_FEE = 0  

    def make_payment(self, order: dict):
        total: float = order.get('total', 0.0)
        final_amount = total + self.TRANSACTION_FEE
        print(f"\n[UPI] Processing payment. Amount: {total} INR + "
              f"Fee: {self.TRANSACTION_FEE},Total = {final_amount} INR")
