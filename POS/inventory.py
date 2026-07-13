from inventory_manager import InventoryManager
class Inventory:
    def __init__(self,database):
        self.db = database
        self.im = InventoryManager(self.db)
        self.check_status = self.im.status
    def addItem(self):
        while True:
            name = input("Enter the name of the product")
            if not name:
                print("Name cannot be empty")
                continue
            while True:
                try:
                    price = float(input("Enter the price of the product"))
                    if price<=0:
                        print("Price must be greater that 0")
                        continue
                    break
                except ValueError:
                    print("Please enter the price in decimal")
            search = self.im.searchByName_Price(name,price)
            if not search['value']: print("There was a problem in the database"); return True
            if search['data']:
                print(f"The product {name} is already present with the price - {price} please select the update part")
                return True
            break
        while True:
            try:
                stock = int(input("Enter the new stock of the product"))
                if stock<0:
                    print("Stock cannot be negative")
                    continue
                break
            except ValueError:
                print("Please enter in digits")
        response = self.im.addInventory(name,price,stock)
        if response['value']:
            print(f"{name} of {price} was successfully added to the inventory")
        else:
            print(f"There was a problem in adding - {response['message']}")
        return True
    def printList(self):
        response = self.im.printList()
        if not response['value']: print("There was problem in the database")
        if not response['data']:
            print("There are no items to display at the moment")
        else:
            print(response['data'])
        return True
    def search(self):
        while True:
            try:
                select = int(input("1. SEARCH BY ID|| 2.SEARCH BY NAME || 3. SEARCH BY NAME AND PRICE"))
                break
            except ValueError:
                print("Please select from the above set of values in digits")
        while True:
            if select == 1:
                while True:
                    try:
                        id = int(input("Please select the id you want to search"))
                        break
                    except ValueError:
                        print("Please provide the value in digits")
                response = self.im.searchById(id)
                if not response['value']:
                    print("There was some problem with the database")
                    break
                if response['data']:
                    print(response['data'])
                else:
                    print("There are no items in the list with the id")
                break
            elif select == 2:
                name = input("Please select the name of the product")
                response = self.im.searchByName(name)
                if not response['value']:
                    print("There was some problem with the database")
                    break
                if response['data']:
                    print(response['data'])
                else:
                    print(f"There are no items with the name - {name}")
                break
            elif select == 3:
                name = input("Please select the item name")
                while True:
                    try:
                        price = float(input("Select the price of the item"))
                        break
                    except ValueError:
                        print("Please select the value in numerical")
                response = self.im.searchByName_Price(name,price)
                if not response['value']:print("There was some problem in the database");break
                if response['data']:
                    print(response['data'])
                else:
                    print(f"The {name} and {price} combo in not availaible")
            else:
                print("Please select from the above list of choice")
                continue
            break
        return True
    def updateName(self,id,current_data):
        name = input("Input the new name that you want to update")
        response = self.im.updateName(id,name)
        if not response['value']: return print("There was problem in the database while updating name")
        return print("Name was updated successfully")
    def updatePrice(self,id,current_data):
        while True:
            try:
                price = float(input("Input the new price of the product"))
                break
            except ValueError:
                print("Please input the value in numerical")
        response = self.im.updatePrice(id,price)
        if response['value']: return print("The price was updated successfully")
        return print("There was problem in the database while updating the price")
    def updateStock(self,id,current_data):
        while True:
            try:
                stock = int(input("Input the new stock"))
                if stock<0:
                    print("The stock value cannot be negative")
                    continue
                break
            except ValueError:
                print("Please enter the stock value in integer")
        current_stock = current_data.get('item_quant',0)
        final_stock = stock+current_stock
        response = self.im.updateStock(id,final_stock)
        if response['value']:
            return print("The stock was updated successfully")
        return print("There was a problem in updating the stock")
    def update(self):
        catlog = self.im.printList()
        print("Welcome to update")
        if not catlog['value']: print("There was a problem in database"); return True
        if not catlog['data']: print("There are no items for update");return True
        print(catlog['data'])
        while True:
            while True:
                try:
                    id = int(input("Select the id you want to make a change"))                        
                    break
                except ValueError:
                    print("Please select the id in digit")
            item_search = self.im.searchById(id)
            if not item_search['value']:
                print("There is problem in the database");return True
            if not item_search['data']:
                print("There is no data witht the selected id.")
                continue
            break
        current_data = item_search['data'][0]
        print(f"This is the product that you selected - {current_data}")
        menu_choice = {"name": lambda: self.updateName(id,current_data),
                       "price": lambda: self.updatePrice(id,current_data),
                       "stock": lambda: self.updateStock(id,current_data)}
        while True:
            choice = input("EDIT - NAME || PRICE || STOCK || EXIT").strip().lower()
            if choice=="exit":
                print("Exiting the update menu")
                break
            elif choice in menu_choice:
                menu_choice[choice]()
                break
            else:
                print("Please select from the above set of choices")
        return True
    def delete(self):
        print_search = self.im.printList()
        if not print_search['value']: print("There was problem in the database");return True
        if not print_search['data']: print("There are no data at the moment");return True
        print(print_search['data'])
        while True:
            try:
                id = int(input("Select the id of the product that you want to delete"))
                break
            except ValueError:
                print("Please input the id in digits")
        search_id = self.im.searchById(id)
        if not search_id['value']:print("There was a problem in the database");return True
        if not search_id['data']:print("There was no product with the particular id"); return True
        print(f"This is the product that you selected - {search_id['data'][0]}")
        while True:
            choose = input("Do you want to delete the product surely?- YES || NO").strip().lower()
            if choose == "yes":
                delete_response = self.im.deleteItem(id)
                if delete_response['value']:
                    print("The product was deleted successfully")
                else:
                    print("There was problem in deleting the product")
                break
            elif choose == "no":
                print("There is a termination of the process. No product was deleted form the table")
                break
            else:
                print("Please select either yes or no")
        return True