"""client Runner"""
from checkout.creditcard_checkout import CreditCardCheckout
from checkout.paypal_checkout import PayPalCheckout
from checkout.upi_checkout import UPICheckout

def run_shopping_cart():
    print("\nShopping Cart Implementation using Template Design Pattern")
    order1 = {
        "items": ["Laptop", "Mouse"],
        "total": 120000,
        "email": "customer@example.com",
        "card_number": "1234-5678-9876-5432"
    }

    order2 = {
        "items": ["Shoes"],
        "total": 800,
        "email": "user@paypal.com",
        "paypal_id": "user123"
    }

    order3 = {
        "items": ["Book"],
        "total": 150,
        "email": "reader@example.com",
        "upi_id": "reader@upi"
    }

    print("\nCheckout With Credit Card")
    checkout=CreditCardCheckout()
    checkout._checkout(order1)

    print("\nCheckout With UPI")
    checkout=UPICheckout()
    checkout._checkout(order2)

    print("\nCheckout with PayPal")
    checkout=PayPalCheckout()
    checkout._checkout(order3)

