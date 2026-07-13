class AdminMange:
    def __init__(self,database):
          self.db = database
          self.status = self.createAdmin()
    def createAdmin(self):
        create_querry = '''CREATE TABLE IF NOT EXISTS admin(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(50) NOT NULL,
                            email VARCHAR(50) NOT NULL UNIQUE,
                            password VARCHAR(50) NOT NULL);'''
        response = self.db.runQuerry(create_querry,)
        return response
    def addAdmin(self,name,email,password):
        add_querry = "INSERT INTO admin(name,email,password) VALUES (?,?,?)"
        response = self.db.runQuerry(add_querry,(name,email,password))
        return response
    def printList(self):
        print_querry = "SELECT * FROM admin"
        response = self.db.runQuerry(print_querry)
        return response
    def searchEmail(self,mail):
        seach_querry = "SELECT * FROM admin WHERE email = ?"
        response = self.db.runQuerry(seach_querry,(mail,))
        return response
    def searchId(self,id):
        search_querry = "SELECT * FROM admin WHERE id = ?"
        response = self.db.runQuerry(search_querry,(id,))
        return response
    def updateName(self,id,name):
        update_querry = "UPDATE admin SET name = ? WHERE id = ?"
        reponse = self.db.runQuerry(update_querry,(name,id))
        return reponse
    def updateEmail(self,id,mail):
        update_querry = "UPDATE admin SET email = ? WHERE id = ?"
        response = self.db.runQuerry(update_querry,(mail,id))
        return response
    def updatePassword(self,id,passw):
        update_querry = "UPDATE admin SET password = ? WHERE id = ?"
        response = self.db.runQuerry(update_querry,(passw,id))
        return response
    def deleteAdmin(self,id):
        delete_querry = "DELETE FROM admin WHERE id=?"
        response = self.db.runQuerry(delete_querry,(id,))
        return response
    def closeDb(self):
        self.db.disconnect()
    def verifyAdmin(self,mail,password):
        search_querry = "SELECT * FROM admin WHERE email = ? AND password = ?"
        response = self.db.runQuerry(search_querry,(mail,password))
        return response
