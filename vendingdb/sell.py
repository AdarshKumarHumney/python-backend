import os
from database import VendingDatabase
from dotenv import load_dotenv
from customer_back import Customer
load_dotenv()
db_name = os.getenv("DB_NAME")
vd = VendingDatabase(db_name)
c = Customer(vd)
print("---Welcome---")
def printProduct():
    value = c.showStock()
    if value['success']:
        print(" ID || NAME || PRICE || QUANTITY ")
        for i in value['data']:
            print(f" {i['id']} || {i['name']} || {i['price']} || {i['stock']}")
    else:
        print(value['message'])
while True:
    printProduct()
    user_select = input("BUY||EXIT").lower().strip()
    if user_select=="buy":
        while True:
            try:
                id_select = int(input("Please select the id of the product that you want to buy"))
                break
            except ValueError:
                print("Please select the id in digits")
                continue
        search_id = c.searchIdStock(id_select)
        if not search_id['success']:
            print(search_id['message'])
            continue
        confirm = input("Are you sure you want to buy this? YES").lower()
        if confirm=="yes":
            buy_confirm = c.buy(id_select)
            if buy_confirm['success']:
                print(f"Enjoy {search_id['data'][1]}")
            else:
                print(buy_confirm['message'])
        else:
            print("Exiting the transaction..")
            continue
    elif user_select=="exit":
        print("Thank you!! VISIT AGAIN")
        break
    else:
        print("Please select from the above option")
        continue
c.connect.connection.close()
vd.connection.close()