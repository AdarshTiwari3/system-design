""" AuthStrategy interface (abstract base class)"""
from abc import ABC, abstractmethod

class AuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, user_data: dict) -> bool:
        pass