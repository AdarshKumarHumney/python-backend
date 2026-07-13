class InventoryManager:
    def __init__(self,database):
        self.db = database
        self.status = self.createInventory()
    def createInventory(self):
        create_querry = '''CREATE TABLE IF NOT EXISTS inventory(
                        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        item_name TEXT NOT NULL,
                        item_price REAL NOT NULL,
                        item_quant INTEGER CHECK(item_quant>=0));'''
        response = self.db.runQuerry(create_querry)
        return response
    def addInventory(self,name,price,stock):
        add_querry = "INSERT INTO inventory(item_name,item_price,item_quant) VALUES(?,?,?)"
        response = self.db.runQuerry(add_querry,(name,price,stock))
        return response
    def searchById(self,id):
        search_querry = "SELECT * FROM inventory WHERE item_id = ?"
        response = self.db.runQuerry(search_querry,(id,))
        return response
    def searchByName(self,name):
        search_querry = "SELECT * FROM inventory WHERE item_name = ?"
        response = self.db.runQuerry(search_querry,(name,))
        return response
    def searchByName_Price(self,name,price):
        search_querry = "SELECT * FROM inventory WHERE item_name = ? AND item_price = ?"
        response = self.db.runQuerry(search_querry,(name,price))
        return response
    def printList(self):
        print_querry = "SELECT * FROM inventory"
        response = self.db.runQuerry(print_querry)
        return response
    def updateName(self,id,name):
        update_querry = "UPDATE inventory SET item_name = ? WHERE item_id = ?"
        response = self.db.runQuerry(update_querry,(name,id))
        return response
    def updatePrice(self,id,price):
        update_querry = "UPDATE inventory SET item_price = ? WHERE item_id = ?"
        response = self.db.runQuerry(update_querry,(price,id))
        return response
    def updateStock(self,id,stock):
        update_querry = "UPDATE inventory SET item_quant = ? WHERE item_id = ?"
        response = self.db.runQuerry(update_querry,(stock,id))
        return response
    def deleteItem(self,id):
        delete_querry = "DELETE FROM inventory where item_id = ?"
        response = self.db.runQuerry(delete_querry,(id,))
        return response