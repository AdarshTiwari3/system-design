"""Base template for checkout process"""

from abc import ABC, abstractmethod
from typing import final

class CheckoutProcess(ABC):
    @final
    def _checkout(self,order:dict):
        """Template method (intended as private)"""
        self.select_item(order)
        self.add_to_cart(order)
        self.make_payment(order)
        self.send_receipt(order)



    def select_item(self, order: dict):
        print(f"\n✔️ Checkout Item Selected={order.get('items')}")

    def add_to_cart(self,order:dict):
        print(f"\n✔️ Item-{order.get('items')} added to cart 🛒, total={order.get('total')}")

    @abstractmethod
    def make_payment(self,order:dict):
        pass

    def send_receipt(self,order:dict):
        print(f"\n✅ Receipt send to {order.get('email')} with order details")
