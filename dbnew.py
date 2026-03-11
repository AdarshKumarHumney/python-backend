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
    cursor.execute(create_table_querry)
    findquerry = "SELECT * FROM user"
    cursor.execute(findquerry)
    usernew = cursor.fetchall()
    if usernew:
        print(User.createDictionary(usernew))
    else:
        print(f"you emptied the database")
    while True:
        userchoice = input("Do you want to enter a new member? Yes/No")
        if userchoice.lower()=="yes":
            new_name = input("Please enter the name")
            new_email = input("Please provide with an email")
            new_age = int(input("please give an age"))
            insert_querry = "INSERT INTO user(name,email,age) VALUES (?, ?, ?)"
            cursor.execute(insert_querry,(new_name,new_email,new_age))
            continue
        elif userchoice.lower()=="no":
            print("See you next time")
            break
        else:
            print("Please answer in yes or no")    
    connection.commit()        
    cursor.execute(findquerry)
    usernew = cursor.fetchall()
    if usernew:
        print(User.createDictionary(usernew))
    else:
        print(f"you emptied the database")
    delete_id = input("Enter the name that you want to delete")
    delete_email = input("Enter the email as well")
    cursor.execute("SELECT * FROM user WHERE name = ? AND email = ?", (delete_id, delete_email))
    print(cursor.fetchall())
    delete_querry = "DELETE FROM user WHERE name= ? AND email = ?"
    cursor.execute(delete_querry,(delete_id,delete_email,))
    connection.commit()
    cursor.execute(findquerry)
    usernew = cursor.fetchall()
    if usernew:
        print(User.createDictionary(usernew))
    else:
        print(f"you emptied the database")    
    connection.close()
except sqlite3.Error as e:    
    print(e)
