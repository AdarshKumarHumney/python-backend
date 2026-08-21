from database import Database
from admin_manager import AdminMange
from inventory import Inventory
from security import Security
from user_manager import UserManager
from admin import Admin
from user import User
import os
from dotenv import load_dotenv
load_dotenv()
db_name = os.getenv("DB_NAME")
db1 = Database(db_name)
am = AdminMange(db1)
um = UserManager(db1)
sec = Security(am,um)
im = Inventory(db1)
Ad1 = Admin(am,im,sec)
Us1 = User(um,sec,im,Ad1)
if not db1.status['value']:
    print("There is problem in the database connection. please try after sometime")
elif not am.status['value']:
    print(f"Problem in creating the admin table - {am.status['message']}")
elif not um.status['value']:
    print(f"Problem in creating the user table -  {um.status['message']}")
else:
    while True:
        select = input("ADMIN || USER || EXIT").lower()
        if select == "admin":
            Ad1.run()
        elif select == "user":
            Us1.run()
        elif select == "exit":
            print("Getting out of system")
            break
        else:
            print("Please choose from the above set of option")
db1.disconnect()
    