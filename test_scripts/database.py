import os
import sqlite3
class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.make_db()
    def make_db(self):
        filelocation = os.path.dirname(__file__)
        new_dir = "testdb"
        new_db = "new_db.db"
        full_dir = os.path.join(filelocation,new_dir)
        os.makedirs(full_dir,exist_ok=True)
        try:
            full_db = os.path.join(full_dir,new_db)
            self.connection = sqlite3.connect(full_db)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(e)
        self.CreateAdminTable()
        self.CreateUserTable()    
    def CreateAdminTable(self):
        create_table_querry = '''CREATE TABLE IF NOT EXISTS admin(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL);'''
        self.cursor.execute(create_table_querry)
        self.connection.commit()
    def CreateUserTable(self):
        create_table_querry = '''CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER NOT NULL);'''
        self.cursor.execute(create_table_querry)
        self.connection.commit()
    def InserIntoAdmin(self,name,email,password):
        insert_querry_admin = "INSERT INTO admin(name, email, password) VALUES (?,?,?)" 
        try:
            self.cursor.execute(insert_querry_admin,(name,email,password,))
            self.connection.commit()
            print("value into admin was added successfully")
        except sqlite3.Error as e:
            print(e)
    def InsertIntoUser(self,name,email,age):
        inser_querry_user = "INSERT INTO user(name,email,age) VALUES (?,?,?)"
        try:
            self.cursor.execute(inser_querry_user,(name,email,age,))
            self.connection.commit()
            return {"value":True,"message":"Successfully entered into User"}
        except sqlite3.Error as e:
            return{"value":False,"message":e}
    def searchDataBase(self,table,field,value):
        search_table_querry = f"SELECT * FROM {table} WHERE {field} = ?"
        self.cursor.execute(search_table_querry,(value,))
        return self.cursor.fetchall()
    def PrintTable(self,choice):
        all_querry = f"SELECT * FROM {choice}"
        self.cursor.execute(all_querry)
        list_user = self.cursor.fetchall()
        return list_user
    def UpdateDatabase(self,table,field,field_value,id_value):
        update_table_querry = f"UPDATE {table} SET {field}=? WHERE id=?"
        try:
            self.cursor.execute(update_table_querry,(field_value,id_value,))
            self.connection.commit()
            return {"value" : True, "message":"Updated Successfully" }
        except sqlite3.Error as e:
            return {"value":False,"message":e}
    def DeleteDatabase(self,table,id):
        delete_database = f"DELETE FROM {table} WHERE id=?"
        try:
            self.cursor.execute(delete_database,(id,))
            self.connection.commit()
            return{"value": True, "message":"Successfully deleted"}
        except sqlite3.Error as e:
            return{"value":False,"message":e}
    def SecurityCheck(self,table,field1,field2,value1,value2):
        search_querry = f"SELECT * FROM {table} WHERE {field1}=? AND {field2}=?"
        try:
            self.cursor.execute(search_querry,(value1,value2,))
            got_result = self.cursor.fetchone()
            return got_result
        except sqlite3.Error:
            return False
