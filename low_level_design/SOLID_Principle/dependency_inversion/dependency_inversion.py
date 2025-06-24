'''
Dependency Inversion- High-level modules should not depend on low-level modules. Both should depend on the abstraction.

This means that a particular class should not depend directly on another class, but on an abstraction (interface) of this class.

Applying this principle reduces dependency on specific implementations and makes our code more reusable.

In Simple Terms:

- Don’t hardcode dependencies (like concrete classes or implementations).
- Instead, rely on interfaces or abstract base classes.
- Let high-level logic depend on what something does, not how it does it

Defining an abstract base class — the key to DIP.
'''

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass

class PostgreSQLDB(Database):
    def connect(self) -> str:
        return "Everthing configured correctly, connected to DB" 
    
class DBService():
    def __init__(self, db: Database):
        self.db=db #depends on Abstraction, what type of Database is used, loose coupling as it can take any db type

    def fetch_data(self) -> str:
        return self.db.connect()
    
def run_dependency_inversion_principle()-> None:

    db=PostgreSQLDB()
    data_service=DBService(db)

    print(data_service.fetch_data())
    

