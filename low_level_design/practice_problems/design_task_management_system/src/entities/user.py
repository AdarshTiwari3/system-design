from uuid import uuid4

class User:
    def __init__(self, name: str, email: str):
        if not name:
            raise ValueError("User name cannot be empty")
        if not email:
            raise ValueError("Email cannot be empty")
        
        self._id: str= str(uuid4())
        self._name= name
        self._email= email
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def email(self) -> str:
        return self._email