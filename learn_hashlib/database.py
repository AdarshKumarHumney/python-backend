import os
import sqlite3
class dataBase:
    def __init__(self):
        file_path = os.path.dirname(__file__)
        self.new_path = os.path.join(file_path,"learn.db")
        self.connection = None
        self.cursor = None
        self.status = self.connect()
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.new_path)
            self.cursor = self.connection.cursor()
        except sqlite3 as e:
            return {"value": False, "message": f"Cannot connect- {e}","data":None}
        return {"value": True, "message": f"Connected successfully","data":None}
    def disconect(self):
        try:
            self.connection.close()
        except sqlite3.Error as e:
            return {"value": False, "message": f"Cannot disconnect- {e}","data":None}
        return {"value": True, "message": f"Disconnected successfully","data":None}
    def runQuerry(self,querry,params = (), autocommit = True):
        if self.status ==False:
            self.connect()
        data = []
        try:
            response = self.cursor.execute(querry,params)
            if querry.strip().startswith("SELECT"):
                attributes = [desc[0] for desc in self.cursor.description]
                list1 = self.cursor.fetchall()
                for i in list1:
                    data.append(dict(zip(attributes,i)))
            else:
                data = None
            if autocommit:
                self.connection.commit()
                return {"value": True, "message": f"querry executed successfully","data":data}
        except sqlite3.Error as e:
            return {"value": False, "message": f"Cannot execute- {e}","data":None}