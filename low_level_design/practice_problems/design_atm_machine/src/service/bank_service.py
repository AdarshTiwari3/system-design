"""Bank Service"""
from threading import Lock
from typing import Dict

from entities.account import Account
from exceptions.domain_exception import (
    AccountNotFoundError,
    InvalidAmountError,
)


class BankService:
    def __init__(self):
        self._accounts: Dict[str, Account]={}  # account_number -> Account
        self._card_to_account: dict[str, str] = {} # card_number -> account_number
        self._lock = Lock()

    def register_account(self, account: Account):
        with self._lock:
            if account.account_number in self._accounts:
                raise ValueError(
                    f"Account {account.account_number} already registered"
                )
            self._accounts[account.account_number] = account

    def link_card_to_account(self, card_number: str, account_number: str):
        with self._lock:
            if account_number not in self._accounts:
                raise AccountNotFoundError("Account does not exist")

            if card_number in self._card_to_account:
                raise ValueError(
                    f"Card {card_number} already linked to an account"
                )

            self._card_to_account[card_number] = account_number


    def _get_account_by_card(self, card_number: str)-> Account:
        with self._lock:
            account_number=self._card_to_account.get(card_number)

        if not account_number:
            raise AccountNotFoundError("No account linked to this card")
        
        account = self._accounts.get(account_number)

        if not account:
            raise AccountNotFoundError("Account not found")

        return account


    def get_balance(self, card_number: str) -> float:
        account = self._get_account_by_card(card_number)
        return account.balance


    def withdraw(self,card_number: str, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Invalid withdrawal amount")
        
        account=self._get_account_by_card(card_number)
        account.withdraw(amount)

    
    def deposit(self, card_number: str, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Invalid deposit amount")

        account = self._get_account_by_card(card_number)
        account.deposit(amount)
