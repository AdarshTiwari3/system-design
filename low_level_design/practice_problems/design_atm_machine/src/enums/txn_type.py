from enum import Enum

class TransactionType(Enum):
    CHECK_BALANCE="CHECK_BALANCE"
    WITHDRAW_CASH="WITHDRAW_CASH"
    DEPOSITE_CASH="DEPOSITE_CASH"