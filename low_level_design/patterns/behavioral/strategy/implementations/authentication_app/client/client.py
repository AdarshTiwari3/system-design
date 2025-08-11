"""Implementation of client runner for Authentication App (Strategy Design Pattern) AuthService that will be consumed by main.py"""
from strategies import *
from context.auth_context import AuthContext
def run_strategy_design():

    print("\nRunning Authentication Strategies based on Strategy Design Pattern")
    """Password based authentication strategy"""
    context= AuthContext(PasswordAuthStrategy())
    context.auth({"username": "admin", "password": "123"})
    context.auth({"username": "admin", "password": "1234"})

    """OAuth based authentication strategy"""
    context.set_strategy(OAuthStrategy())
    context.auth({"token":"invalid_oauth_token"})
    context.auth({"token":"valid_oauth_token"})

    """OTP based Authentication Strategy"""

    context.set_strategy(OTPAuthStrategy())
    context.auth({"otp": "24567"})
    context.auth({"otp": "234567"})



    
    