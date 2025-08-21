"""client runner"""
from context.vending_machine import VendingMachine

def run_vending_machine():
    print(f"\nRunning Vending Machine")
    inventory = {
        "item-0123": {"name": "Coke", "price": 20, "stock": 2},
        "item-0124": {"name": "Chips", "price": 10, "stock": 1},
        "item-0125": {"name": "Pop-corn", "price": 39.0, "stock": 2},
        "item-0126": {"name": "Milk", "price": 56.0, "stock": 1},
    }

    machine = VendingMachine(inventory)
    item_code="item-0126"
    machine.select_item(item_code)
    price=machine.get_item_price(item_code)
    machine.pay_the_amount(price)
    machine.dispense_item()

    print()
    item_code="item-0123"
    machine.select_item(item_code)
    price=machine.get_item_price(item_code)
    machine.pay_the_amount(1)
    machine.dispense_item()

    print()
    item_code="item-0126"
    machine.select_item(item_code)
    price=machine.get_item_price(item_code)
    machine.pay_the_amount(price)
    machine.dispense_item()

    print("\nupdated inventory=",inventory)
    





    