import os
from dotenv import load_dotenv
from database import VendingDatabase
from adminVen import Admin
load_dotenv()
admin_password = os.getenv("Password")
db_name = os.getenv("DB_NAME")
Vd1 = VendingDatabase(db_name)
ad = Admin(Vd1)
print("--Welcome Admin--")
count=3
admin_check = False
def addToMachine():
    max_stock = 30.0
    while True:
        name = input("Enter the name of the product").strip()
        price = input("Enter the price of the product").strip()
        stock = input("Enter stock of the product").strip()
        response = ad.verify(name,price,stock)
        if response[1]:
            print(f"Product cannot be added because of - {response[1]}")
            continue
        name = response[0]['name']
        price = response[0]['price']
        stock_input = response[0]['stock']
        search_stock = ad.searchStock(name,price)
        if search_stock['success']:
            new_stock = min(max_stock,stock_input)
            current_stock = search_stock['data'][3]
            stock = min(max_stock,current_stock+new_stock)
            new_added = stock-current_stock
            discarded = stock_input-new_added
            response = ad.updateStock(name,price,stock)
            if response['success']:
                print(f"{response['message']}. The new stock added-- {new_added}|| The stock discarded-- {discarded}|| The new total in inventory-- {stock}")
            else:
                print(response['message'])
        else:
            stock = min(max_stock,stock_input)
            response = ad.addStock(name,price,stock)
            if response['success']:
                print(response['message'])
            else:
                print(response['message'])
        break    
    return True
def printProduct():
    response = ad.showStock()
    if response['success']:
        for i in response['data']:
            print(f"ID-{i[0]} || PRODUCT-{i[1]} || PRICE-{i[2]} || STOCK-{i[3]}")
    else:
        print(response['message'])
    return True
def Exit():
    exit_choice = input("Press YES to exit").lower()
    if exit_choice=="yes":
        return False
    else:
        return True
def functionGenerator(menu_function):
    keys = list(menu_function.keys())
    return " | ".join(keys).upper()
def prodChcek():
    prod = ad.showStock()
    prod_key = ['id','name','price','quant']
    prod_list = []
    if prod['success']:
        for i in prod['data']:
            if i[3]==0:
                prod_list.append(dict(zip(prod_key,i)))
    if prod_list:
        print("...ALERT...")
        print("Products are out of stock please fill the stock or delete the item from the inventory")
        print(f"{prod_list}")
while count>0:
    admin_pass = input("Please input the admin password to proceed further...").strip()
    if admin_pass == admin_password:
        admin_check = True
        break
    else:
        print("The password you entered is wrong please try again")
        count-=1
if admin_check:
    prodChcek()
    menu_function = {"add":addToMachine,
                "view":printProduct,
                "exit":Exit}
    menu = functionGenerator(menu_function)
    while True:
        input_choice = input(f"Select from {menu}").lower()
        if input_choice in menu_function:
            reponse = menu_function[input_choice]()
            if not reponse:
                print("Exiting Vending machine")
                break
        else:
            print(f"{input_choice} is not in the list of choices above")
else:
    print("Logging out due to incorrect password")
ad.connect.connection.close()