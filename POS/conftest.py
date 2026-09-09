import pytest
from database import Database
from user_manager import UserManager
from inventory_manager import InventoryManager
from inventory import Inventory
@pytest.fixture
def db():
    database = Database(":memory:")
    yield database
    database.disconnect()
@pytest.fixture
def userflow(db):
    inv = InventoryManager(db)
    usm = UserManager(db)
    return {"inv": inv, "usm": usm, "db":db}
@pytest.fixture
def cli_inv(db):
    inv1 = Inventory(db)
    return inv1