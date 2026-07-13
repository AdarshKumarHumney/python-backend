from database import Database
from admin_manager import AdminMange
from inventory import Inventory
from security import Security
import os
from dotenv import load_dotenv
load_dotenv()
db_name = os.getenv("DB_NAME")
db1 = Database(db_name)
    while allow_admin_connect:
        if am.status['value'] and im.check_status['value']:
            print(f"Admin Table creation - {am.status['message']}")
            print(f"Inventory Table creation- {im.check_status['message']}")
            s1 = Security(am)
            allow_next = True
        else:
            print(f"Admin Table creattion- {am.status['message']}")
            print(f"Inventory Table creation- {im.check_status['message']}")
            allow_next=False
        break