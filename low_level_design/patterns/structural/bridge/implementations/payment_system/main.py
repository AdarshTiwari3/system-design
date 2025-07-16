"""Client runner of bridge design pattern"""

from methods.credit_card_payment import CreditCardPayment
from methods.upi_payment import UPIPayment
from methods.netbanking_payment import NetbankingPayment
from gateways.pay_u_gateway import PayUGateway
from gateways.razorpay_gateway import RazorpayGateway
from gateways.stripe_gateway import StripeGateway



def run_client_bridge_pattern():

    print("\nCredit Card payment using Stripe Gateway")
    cc_payment=CreditCardPayment(StripeGateway())
    amount=1200
    cc_payment.pay(amount)

    print("\nPayment using UPI via Razorpay Gatway")
    upi_payment=UPIPayment(RazorpayGateway())
    amount=2500
    upi_payment.pay(amount)

    print("\nPayment using netbanking via PayU Gateway")
    netbanking_payment=NetbankingPayment(PayUGateway())
    amount=1399.779
    netbanking_payment.pay(amount)


    print("\nUPI using PayU gateway")
    upi_payment=UPIPayment(PayUGateway())
    upi_payment.pay(amount)








if __name__ == "__main__":
    print("\nBridge Design Pattern")
    run_client_bridge_pattern()
