import os
import sqlite3
class Database:
    def __init__(self, db_name):
        cur_dir = os.path.dirname(__file__)
        self.db_path = os.path.join(cur_dir,db_name)
        self.connection = None
        self.cursor = None
        self.status = self.connect()
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            return{"value": True, "message": "Database is connected","data":None}
        except sqlite3.Error as e:
            return{"value": False,"message":f"There was a problem - {e}","data":None}
    def disconnect(self):
        self.connection.close()
    def runQuerry(self,querry,params = (), autocommit = True):
        if self.connection is None:
            self.connect()
        data = []
        try:
            self.cursor.execute(querry,params)
            if querry.strip().upper().startswith("SELECT"):
                attributes = [desc[0] for desc in self.cursor.description]
                list1 = self.cursor.fetchall()
                for i in list1:
                    data.append(dict(zip(attributes,i)))
            else:
                data = None
            if autocommit:
                self.connection.commit()
            return {"value": True,"message":"querry executed successfully","data":data,"rowcount":self.cursor.rowcount,"lastrowid":self.cursor.lastrowid}
        except sqlite3.ProgrammingError as e:
            return {"value":False,"message":f"Connection error - {e}","data":None}
        except sqlite3.Error as e:
            if not autocommit:
                self.connection.rollback()
            return{"value":False,"message":f"There was a problem-{e}","data":None}
    def commitTransaction(self):
        try:
            self.connection.commit()
            return{"value":True,"message":f"The commit happened successfully","data":None}
        except sqlite3.Error as e:
            return{"value":False,"message":f"There was a problem-{e}","data":None}
    def rollbackTransaction(self):
        try:
            self.connection.rollback()
            return{"value":True,"message":f"RollBack happened successfully","data":None}
        except sqlite3.Error as e:
            return{"value":False,"message":f"There was a problem-{e}","data":None}