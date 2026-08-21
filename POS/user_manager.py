class UserManager:
    def __init__(self,db):
        self.db = db
        self.status = self.create_table()
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
    def updateName(self,mail,name):
        update_querry = "UPDATE user SET user_name = ? WHERE user_email = ?"
        update_response = self.db.runQuerry(update_querry,(name,id))
        return update_response
    def updateEmail(self,email,mail):
        update_querry = "UPDATE user SET user_email = ? WHERE user_email = ?"
        update_response = self.db.runQuerry(update_querry,(mail,email))
        return update_response
    def updatePassword(self,mail,passw):
        update_querry = "UPDATE user SET user_pass = ? WHERE user_email = ?"
        update_response = self.db.runQuerry(update_querry,(passw,mail))
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
        delete_querry = "DELETE FROM user WHERE user_email = ?"
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
    def createSaleTable(self):
        create_table = '''CREATE TABLE IF NOT EXISTS sale(
                        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        total_amount REAL NOT NULL CHECK(total_amount>=0),
                        sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE);'''
        response = self.db.runQuerry(create_table)
        return response
    def createSaleItem(self):
        create_table = '''CREATE TABLE IF NOT EXISTS sale_item(
                        sale_id INTEGER NOT NULL,
                        item_id INTEGER NOT NULL,
                        item_name VARCHAR(50) NOT NULL,
                        item_quant INTEGER NOT NULL CHECK(item_quant>0),
                        price_at_purchase REAL NOT NULL CHECK(price_at_purchase>=0),
                        PRIMARY KEY(sale_id,item_id),
                        FOREIGN KEY (sale_id) REFERENCES sale(sale_id) ON DELETE CASCADE,
                        FOREIGN KEY (item_id) REFERENCES inventory(item_id)
                        );'''
        response = self.db.runQuerry(create_table)
        return response
    def addToSale(self,user_id,total_amount):
        add_querry = "INSERT INTO sale (user_id,total_amount) VALUES (?,?)"
        response = self.db.runQuerry(add_querry,(user_id,total_amount), autocommit = False)
        return response
    def addToSaleItem(self,sale_id,item_id,item_name,item_quant,price):
        add_querry = "INSERT INTO sale_item(sale_id,item_id,item_name,item_quant,price_at_purchase) VALUES (?,?,?,?,?)"
        response = self.db.runQuerry(add_querry,(sale_id,item_id,item_name,item_quant,price), autocommit = False)
        return response
    def checkoutCart(self,user_id):
        querry = '''SELECT c.item_id,
                    c.item_quant,
                    i.item_name,
                    i.item_price,
                    i.item_quant AS stock
                    FROM cart c
                    INNER JOIN inventory i ON c.item_id = i.item_id
                    WHERE c.user_id = ?'''
        response = self.db.runQuerry(querry,(user_id,))
        return response
    def seeSale(self,user_id):
        see = "SELECT * FROM sale WHERE user_id = ?"
        response = self.db.runQuerry(see,(user_id,))
        return response
    def saleItem(self,sale_id):
        querry = "SELECT * FROM sale_item WHERE sale_id = ?"
        response = self.db.runQuerry(querry,(sale_id,))
        return response
    def checkout(self,user_id):
        getcart = self.checkoutCart(user_id)
        if not getcart['value'] or not getcart['data']:
            return{"value":False,"message":"There was no item in cart or there was some problem in the database","data":None}
        for i in getcart['data']:
            if i['item_quant']>i['stock']:
                return{"value":False,"message":f"{i['item_name']} has more quantity than stock please reduce the quantity and try again","data":None}
        try:
            for i in getcart['data']:
                update = "UPDATE inventory SET item_quant = item_quant-? WHERE item_id = ? and item_quant>=?"
                response = self.db.runQuerry(update,(i['item_quant'],i['item_id'],i['item_quant']),autocommit = False)
                if not response['value']:
                    self.db.rollbackTransaction()
                    return{"value":False,"message":f"There was problem in update - {i['item_name']}","data":None}
                if response.get('rowcount',0)==0:
                    self.db.rollbackTransaction()
                    return{"value":False,"message":f"The stock was high for-{i['item_name']}","data":None}
            delete = "DELETE FROM cart WHERE user_id = ?"
            response = self.db.runQuerry(delete,(user_id,),autocommit = False)
            if not response['value']:
                self.db.rollbackTransaction()
                return{"value":False,"message":f"There was problem in deleting the cart","data":None}
            return{"value":True,"message":f"checkout completed","data":getcart['data']}
        except Exception as e:
                self.db.rollbackTransaction()
                return{"value":False,"message":f"The problem -{e}","data":None}
    def closeDb(self):
        self.db.disconnect()
    