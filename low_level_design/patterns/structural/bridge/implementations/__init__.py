""" code structure """

# payment_system/
# ├── gateways/      
# │   ├── stripe_gateway.py
# │   ├── razorpay_gateway.py
# │   └── gateway.py          # Interface (implementor)
# ├── methods/        
# │   ├── credit_card_payment.py
# │   ├── upi_payment.py
# │   └── payment.py          # Abstraction

# Abstraction defines the "what to do", and delegates "how to do it" to the Implementor

"""Explanation:
1. There are two main components: the Abstraction (e.g., Payment) and the Implementor interface (e.g., Gateway).
2. The Abstraction class holds a reference to the Implementor — this is a composition ("has-a") relationship, meaning the abstraction owns the implementor.
3. The two hierarchies (Abstraction and Implementor) are connected via a "bridge", allowing them to vary independently.
4. This design promotes loose coupling between components and avoids tight inheritance hierarchies.
5. It also prevents class explosion from combinatorial subclassing and was introduced to solve that extensibility problem.
"""