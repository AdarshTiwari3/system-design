"""Implementation of different type of strategies"""
from strategies.oauth_auth import OAuthStrategy
from strategies.otp_auth import OTPAuthStrategy
from strategies.password_auth import PasswordAuthStrategy

__all__=[
    "OAuthStrategy",
    "OTPAuthStrategy",
    "PasswordAuthStrategy"
]