class User:
    def __init__(self,db):
        self.db = db
        self.status = self.create_table
    def create_table(self):
        create_querry = '''CREATE TABLE IF NOT EXISTS user(
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_name TEXT NOT NULL,
                        user_email TEXT NOT NULL UNIQUE,
                        user_pass TEXT NOT NULL);'''
        create_response = self.db.runQuerry(create_querry)
        return create_response
    def cartTable(self):
        create_querry = '''CREATE TABLE IF NOT EXISTS cart(
                        user_id INTEGER NOT NULL,
                        item_id INTEGER NOT NULL,
                        item_quant INTEGER NOT NULL CHECK(item_quant>0),
                        PRIMARY KEY(user_id,item_id),
                        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
                        FOREIGN KEY (item_id) REFERENCES inventory(item_id));'''
        return self.db.runQuerry(create_querry)
    def addUser(self,name,email,password):
        add_querry = "INSERT INTO user (user_name,user_email,user_pass) VALUES (?,?,?)"
        add_response = self.db.runQuerry(add_querry,(name,email,password))
        return add_response
    def verifyUser(self,mail,password):
        verify_querry = "SELECT * FROM user WHERE user_email = ? AND user_pass = ?"
        verify_response = self.db.runQuerry(verify_querry,(mail,password))
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
    def deleteUser(self,mail):
        delete_querry = "DELETE * FROM user WHERE user_email = ?"
        delete_response = self.db.runQuerry(delete_querry,(mail,))
        return delete_response
    def showCart(self,id):
        search_cart = '''SELECT
                    c.item_id,
                    i.item_name,
                    i.item_price,
                    c.item_quant
                    FROM cart c
                    INNER JOIN inventory i ON c.item_id = i.item_id
                    WHERE c.user_id = ?'''
        search_response = self.db.runQuerry(search_cart,(id,))
        return search_response
    def addToCart(self,user_id,item_id,quant):
        add_querry = '''INSERT INTO cart(user_id,item_id,item_quant) VALUES (?,?,?)
                        ON CONFLICT (user_id,item_id)
                        DO UPDATE SET item_quant = item_quant+excluded.item_quant'''
        add_response = self.db.runQuerry(add_querry,(user_id,item_id,quant))
        return add_response
    def updateCart(self,user_id,item_id,quant):
        update_querry = "UPDATE cart SET item_quant = ? WHERE user_id = ? AND item_id = ?"
        response = self.db.runQuerry(update_querry,(quant,user_id,item_id))
        return response
    def searchCartId(self,id):
        search_querry = "SELECT * FROM cart WHERE item_id = ?"
        response = self.db.runQuerry(search_querry,(id,))
        return response
    def showItem(self,usid,iid):
        search = '''SELECT
                c.item_id,
                i.item_name,
                i.item_price,
                c.item_quant
                FROM cart c
                INNER JOIN inventory i ON c.item_id = i.item_id
                WHERE c.user_id = ? AND c.item_id = ?'''
        response = self.db.runQuerry(search,(usid,iid))
        return response
    def closeDb(self):
        self.db.disconnect()
    