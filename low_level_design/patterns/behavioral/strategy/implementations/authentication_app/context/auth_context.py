"""Implementation of Auth Context"""

from interfaces.auth_strategy import AuthStrategy
class AuthContext:
    """references the strategies"""
    def __init__(self, strategy: AuthStrategy) -> None:
        self.__strategy=strategy

    """sets strategy at run time"""
    def set_strategy(self, strategy: AuthStrategy):
        self.__strategy=strategy


    def auth(self, user_data: dict[str,str]) -> bool:
        return self.__strategy.authenticate(user_data)