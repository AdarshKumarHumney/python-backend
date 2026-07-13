class User:
    def __init__(self,db):
        self.db = db
        self.status = self.create_table
    def create_table(self):
        create_querry = '''CREATE TABLE IF NOT EXIST user(
                        user_id INTEGER PRIMARY ID AUTO INCREMENT,
                        user_name TEXT NOT NULL,
                        user_email TEXT NOT NULL UNIQUE,
                        user_pass TEXT NOT NULL);'''
        create_response = self.db.runQuerry(create_querry)
        return create_response
    def addUser(self,name,email,password):
        add_querry = "INSERT INTO user (user_name,user_email,user_pass) VALUES (?,?,?)"
        add_response = self.db.runQuerry(add_querry,(name,email,password))
        return add_response
    def verifyUser(self,mail,password):
        verify_querry = "SELECT * FROM user WHERE user_email = ? AND user_pass = ?"
        verify_response = self.db.runQuerry(verify_querry(mail,password))
        return verify_response
    def printUser(self):
        print_querry = "SELECT * FROM user"
        print_response = self.db.runQuerry(print_querry)
        return print_response
    def updateName(self,id,name):
        update_querry = "UPDATE user SET user_name = ? WHERE user_id = ?"
        update_response = self.db.runQuerry(update_querry,(name,id))
        return update_response
    def updateEmail(self,id,mail):
        update_querry = "UPDATE user SET user_email = ? WHERE user_id = ?"
        update_response = self.db.runQuerry(update_querry,(mail,id))
        return update_response
    def updatePassword(self,id,passw):
        update_querry = "UPDATE user SET user_pass = ? WHERE user_id = ?"
        update_response = self.db.runQuerry(update_querry,(passw,id))
        return update_response
    def searchId(self,id):
        search_id = "SELECT * FROM user WHERE user_id = ?"
        search_response = self.db.runQuerry(search_id,(id,))
        return search_response
    def searchName(self,name):
        search_name = "SELECT * FROM user WHERE user_name = ?"
        search_response = self.db.runQuerry(search_name,(name,))
        return search_response
    def searchEmail(self,mail):
        search_mail = "SELECT * FROM user WHERE user_email = ?"
        search_response = self.db.runQuerry(search_mail,(mail,))
        return search_response
    