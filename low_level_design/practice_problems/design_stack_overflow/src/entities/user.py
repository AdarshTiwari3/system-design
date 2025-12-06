"""User class"""
from uuid import uuid4
import threading

class User:
    def __init__(self, username:str):
        self.user_id:str=str(uuid4())
        self.username:str= username
        self.reputation: int =0
        self._lock=threading.Lock() # to achieve concurrency

    def get_username(self) -> str:
        return self.username
    
    def get_user_id(self) -> str:
        return self.user_id
    
    def get_reputation(self) -> int:
        return self.reputation
    
    def update_reputation(self, earned_reputation: int) -> int:
        with self._lock:
            self.reputation+=earned_reputation
            return self.reputation
