"""Content- Abstract class that will be used in Question, Answer, Comment and Post"""
from abc import ABC
from entities.user import User
from datetime import datetime

class Content(ABC):
    def __init__(self, content_id: str, body: str, author: User):
        self.content_id=content_id
        self.body=body
        self.author=author
        self.created_at : datetime =datetime.now()


    def get_content_author(self) -> User:
        return self.author
    
    def get_content_id(self) -> str:
        return self.content_id
    
    def get_content_body(self) -> str:
        return self.body
    
    def get_content_created_at(self) -> datetime:
        return self.created_at
    
    