"""ATM service implementation this will handle the chain setup and processing the request"""
from core.interface_handler import IHandler
from core.request import ATMRequest
class ATMService:
    def __init__(self, chain: IHandler):
        self.chain=chain

    def withdraw(self,amount:int):
        if amount % 100 != 0:
            print(f"Cannot dispense {amount}: ATM only supports multiples of 100")
            return
        request=ATMRequest(amount)
        self.chain.handle(request)

