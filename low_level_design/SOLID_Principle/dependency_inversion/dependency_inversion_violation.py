
'''
DIP= A particular class should not depend directly on another class, but on an abstraction (interface) of this class.

'''

class PostgreSQLDataBase:
    def connect(self):
        return "connected to database"
    

class DBService:
    def __init__(self):
        self.db=PostgreSQLDataBase() #tightly coupled

    def fetch_data(self):
        return self.db.connect()
        

data_service=DBService()

print(data_service.fetch_data())

#how violation----
"""
DIP Violation
DBService (the high-level class) directly depends on PostgreSQLDataBase (a low-level class).

If you later want to:

Switch to MySQLDatabase

Add logging

Test with a mock database
→ you'd need to modify DBService, which breaks modularity and violates OCP (Open/Closed Principle) as well

"""