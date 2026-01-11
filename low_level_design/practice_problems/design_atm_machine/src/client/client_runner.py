"""Client runner"""

from service.auth_service import AuthService
from service.bank_service import BankService
from service.cash_dispenser import CashDispenser
from core.atm import ATM
from entities.card import Card
from datetime import date
from enums.txn_type import TransactionType
from entities.account import Account


def main():
    print("ATM Machine Running...")

    auth_service = AuthService()
    bank_service = BankService()
    cash_dispenser = CashDispenser()

    # ---------------- BANK SETUP ----------------
    account1 = Account("Acc-0001", "John Doe", 12000)
    account2 = Account("Acc-0002", "Andy", 10000)
    account3 = Account("Acc-0003", "Romy", 2000)

    bank_service.register_account(account1)
    bank_service.register_account(account2)
    bank_service.register_account(account3)

    # ---------------- CARDS ----------------
    card1 = Card("1234-5678-0910-1112", date(2030, 1, 1))
    card2 = Card("2345-1234-8790-1234", date(2029, 2, 2))
    card3 = Card("1245-3435-3490-0941", date(2032, 9, 10))

    bank_service.link_card_to_account(card1.card_number, account1.account_number)
    bank_service.link_card_to_account(card2.card_number, account2.account_number)
    bank_service.link_card_to_account(card3.card_number, account3.account_number)

    # ---------------- AUTH ----------------
    auth_service.register_pin(card1.card_number, "1234")
    auth_service.register_pin(card2.card_number, "2345")
    auth_service.register_pin(card3.card_number, "1243")

    # ---------------- ATM ----------------
    atm = ATM(auth_service, bank_service, cash_dispenser)

    # Wrong PIN -> correct PIN
    atm.insert_card(card1)
    atm.enter_pin("123")

    atm.insert_card(card1)
    atm.enter_pin("1234")
    atm.select_transaction(TransactionType.WITHDRAW_CASH, 3100)
    atm.process_transaction()

    # Deposit
    atm.insert_card(card2)
    atm.enter_pin("2345")
    atm.select_transaction(TransactionType.DEPOSITE_CASH, 3000)
    atm.process_transaction()

    # Balance check
    atm.insert_card(card3)
    atm.enter_pin("1243")
    atm.select_transaction(TransactionType.CHECK_BALANCE)
    atm.process_transaction()

    # Insufficient balance
    atm.insert_card(card3)
    atm.enter_pin("1243")
    atm.select_transaction(TransactionType.WITHDRAW_CASH, 35000)
    atm.process_transaction()


