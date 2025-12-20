"""comment by user"""

from uuid import uuid4
from entities.user import User
from datetime import datetime

class Comment:
    def __init__(self, content: str, author: User):
        self._id=str(uuid4())
        self._content= content
        self._author= author
        self._timestamp= datetime.now()

    @property
    def author(self) -> User:
        return self._author
    
    @property
    def content(self) -> str:
        return self._content
        