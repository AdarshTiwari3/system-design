"""
Domain Exception represents a business rule violation - not a programming error and not a system failure.
Example - Account, Transaction errors

"""
class DomainException(Exception):
    pass


class InsufficientBalanceError(DomainException):
    pass


class AccountNotFoundError(DomainException):
    pass


class InvalidAmountError(DomainException):
    pass
