import sqlite3
import os
class User:
    @staticmethod
    def createDictionary(alluser):
        return{
            i[0] : {
            "name":i[1],
            "email":i[2],
            "age":i[3]
        }for i in alluser
        }   
current_path = os.path.dirname(__file__)
dir_name = "database"
db_name = "my_app.db"
dir_path = os.path.join(current_path,dir_name)
os.makedirs(dir_path,exist_ok=True)
full_path = os.path.join(dir_path,db_name)
try:
    connection = sqlite3.connect(full_path)
    cursor = connection.cursor()
    print("Database initialised")
    create_table_querry = """
    CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER
    );
    """
    findname = "Anand"
    findquerry = "SELECT * FROM user WHERE name = ?"
    cursor.execute(create_table_querry)
    cursor.execute(findquerry,(findname,))
    usernew = User.createDictionary(cursor.fetchall())
    connection.commit()
    for i,details in usernew.items():
        print(f"{i}->{details}") 
    connection.close()
except sqlite3.Error as e:    
    print(e)
