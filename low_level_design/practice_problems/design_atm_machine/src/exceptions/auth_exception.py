"""Auth Exception handler"""

class AuthenticationError(Exception):
    pass

class InvalidPINError(AuthenticationError):
    pass
