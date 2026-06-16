import sqlite3
import os
class VendingDatabase:
    def __init__(self,db_name):
        file_path = os.path.dirname(__file__)
        db_path = os.path.join(file_path,db_name)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.createTable()
    def createTable(self):
        table_create = '''CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL)'''
        self.cursor.execute(table_create)
        self.connection.commit()
    def addInventory(self,name,price,stock):
        insert_query = "INSERT INTO product(name,price,stock) values (?,?,?)"
        try:
            self.cursor.execute(insert_query,(name,price,stock))
            self.connection.commit()
            return {"success":True,"message":"Data entered into table successfully"}
        except sqlite3.Error as e:
            return {"success":False,"message":f"Data was not able to be inserted into table because-- {e}"}
    def showInventory(self):
        show_query = "SELECT * FROM product"
        try:
            self.cursor.execute(show_query)
            value = self.cursor.fetchall()
            return {"success":True,"message":f"Here are the list of products", "data":value}
        except sqlite3.Error as e:
            return {"success":False,"message":f"Data was not able to be inserted into table because-- {e}", "data":None}
    def searchInventory(self,name,price):
        search_query= "SELECT * FROM product where name = ? and price = ?"
        try:
            self.cursor.execute(search_query,(name,price))
            value = self.cursor.fetchone()
            if value:
                return {"success":True,"message":"Product found", "data":value}
            else:
                return {"success":False,"message": "Product not found", "data":None}
        except sqlite3.Error as e:
            return {"success":False,"message":f"Data was not able to be inserted into table because-- {e}", "data":None}
    def searchId(self,id):
        search_query = "SELECT * FROM product WHERE id = ?"
        try:
            self.cursor.execute(search_query,(id,))
            value = self.cursor.fetchone()
            if value:
                return {"success":True,"message":"Product found", "data":value}
            else:
                return {"success":False,"message": "Product not found", "data":None}
        except sqlite3.Error as e:
            return {"success":False,"message":f"Data was not able to be inserted into table because-- {e}", "data":None}
    def updateInventory(self,name,price,stock):
        update_query = "UPDATE product SET stock = ? WHERE name = ? AND price = ?"
        try:
            self.cursor.execute(update_query,(stock,name,price))
            self.connection.commit()
            return {"success":True,"message":"Data was updated successfully", "data":None}
        except sqlite3.Error as e:
            return {"success":False,"message":f"Data was not able to be inserted into table because-- {e}", "data":None}
    def updateBuy(self,id):
        update_query = "UPDATE product SET stock = stock-1 WHERE id = ? AND stock>0"
        try:
            self.cursor.execute(update_query,(id,))
            if self.cursor.rowcount>0:
                self.connection.commit()
                return {"success":True,"message":"Data was updated successfully", "data":None}
            else:
                return {"success":False,"message":"Items not availaible or out of stock", "data":None}
        except sqlite3.Error as e:
            return {"success":False,"message":f"Data was not able to be inserted into table because-- {e}", "data":None}