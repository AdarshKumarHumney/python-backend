import pytest
from database import Database
from user_manager import UserManager
from inventory_manager import InventoryManager
from admin_manager import AdminMange
from admin import Admin
from security import Security
from inventory import Inventory
@pytest.fixture
def db():
    database = Database(":memory:")
    yield database
    database.disconnect()
@pytest.fixture
def userflow(db):
    inv = InventoryManager(db)
    adm = AdminMange(db)
    usm = UserManager(db)
    return {"inv": inv, "adm": adm,"usm":usm, "db":db}
@pytest.fixture
def cli_ad(db,userflow):
    inv = Inventory(db)
    sec = Security(userflow['adm'],userflow['usm'])
    ad1 = Admin(userflow['adm'],inv,sec)
    return ad1