"""Account - it holds account details"""
from entities.card import Card
from typing import Dict
from threading import Lock
from exceptions.domain_exception import InsufficientBalanceError


class Account:
    def __init__(self, account_number: str, customer_name: str, balance: float):
        self._account_number: str = account_number
        self._balance=balance
        self._cards: Dict[str, Card]={}
        self.customer_name=customer_name
        self._lock=Lock()

    @property
    def account_number(self) -> str:
        return self._account_number
    
    @property
    def balance(self) -> float:
        return self._balance
   
    def get_cards(self) -> Dict[str, Card]:
        with self._lock:
            return dict(self._cards)
    
    def add_card(self, card: Card):
        with self._lock:
            self._cards[card.card_number] = card

    def remove_card(self, card_number: str):
        with self._lock:
            self._cards.pop(card_number, None)

    
    def deposit(self, amount: float):
        if amount<0:
            raise ValueError("Invaild Amount")
        
        with self._lock:
            self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Invalid amount")
         
        with self._lock:
            if self._balance < amount:
                raise InsufficientBalanceError("Insufficient balance")
            
            self._balance -= amount
            
