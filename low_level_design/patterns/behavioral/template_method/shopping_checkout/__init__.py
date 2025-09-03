"""
Use the pattern when you have several classes that contain almost identical algorithms with some minor differences. As a result, you might need to modify all classes when the algorithm changes.

When you turn such an algorithm into a template method, you can also pull up the steps with similar implementations into a superclass, eliminating code duplication. Code that varies between subclasses can remain in subclasses.


In our case:
1. Checkout flow as the template method

2. Payment methods (CreditCard, PayPal, UPI, etc.) as concrete subclasses
Template Method (skeleton):

    Select items
    Add to cart
    Make payment
    Send receipt

Concrete implementations:

    Credit card payment
    PayPal payment
    UPI


"""