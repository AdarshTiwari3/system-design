"""
Domain Exception represents a business rule violation - not a programming error and not a system failure.
Example - Account, Transaction errors

"""
class InsufficientBalanceError(Exception):
    pass
