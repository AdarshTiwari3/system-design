import pytest
from low_level_design.SOLID_Principle.dependency_inversion.dependency_inversion import (Database, DBService, PostgreSQLDB)

# -------------------------------
# 1. Unit Test with Mock Database
# -------------------------------

class MockDatabase(Database):
    def connect(self) -> str:
        return "Mock DB connected"

@pytest.fixture
def mock_db() -> Database:
    return MockDatabase()

@pytest.fixture
def db_service_with_mock(mock_db: Database) -> DBService:
    return DBService(mock_db)

def test_fetch_data_with_mock_db(db_service_with_mock: DBService):
    assert db_service_with_mock.fetch_data() == "Mock DB connected"


# -------------------------------
# 2. Integration Test with Real DB
# -------------------------------

@pytest.fixture
def real_postgres_db() -> Database:
    return PostgreSQLDB()

@pytest.fixture
def db_service_with_real_db(real_postgres_db: Database) -> DBService:
    return DBService(real_postgres_db)

def test_fetch_data_with_real_db(db_service_with_real_db: DBService):
    assert db_service_with_real_db.fetch_data() == "Everthing configured correctly, connected to DB"
