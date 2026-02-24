import random
import time
import os
import json
script_location = os.path.dirname(__file__)
filelocation = os.path.join(script_location,"stock.json")
try:
    with open(filelocation,"r") as f:
        inventory = json.load(f)
        print("File loaded successfully")
except FileNotFoundError:        
    print("File not found at the location")
    inventory = {
    'soda': {'price': 20, 'stock': 5},
    'chips': {'price': 10, 'stock': 3},
    'cookie': {'price': 5, 'stock': 10}
    }
cart = []
cart_total = 0
count = 0
while True:
    print("Welcome, what would you like to have")
    for i,j in inventory.items():
        print(f"{i} is availaible at {j['price']} and we have {j['stock']} left")
    userwant = input("Do you want to buy or pay")
    if userwant.lower() == "buy":
        userinput = input("What do you want to buy").lower()
        if userinput in inventory:
                details = inventory[userinput]
                if details['stock']==0:
                    print("Not in stock")
                    break
                else:
                    needstock = int(input("How much you want to buy"))
                    if needstock <= details['stock']:
                        print(f"{userinput} added to cart")
                        cart.append(details['price']*needstock)
                        details['stock']-=needstock
                        print("Item added successfully")
                        with open(filelocation,"w") as g:
                            json.dump(inventory,g)
                        print("Item saved successfully")    
                    else:
                        print("What you are looking is more than the stock")         
    elif userwant.lower() == "pay":
        if len(cart)==0:
            print("Nothing in the cart")
            break
        else:    
            for i in cart:
                cart_total = cart_total+i
        print("generating discount for you")
        discount = random.randint(0,20)
        print("your discount is...")
        time.sleep(2)
        print(f"{discount}")
        new_total = cart_total-(cart_total*discount/100)
        print(f"your new bill is..")
        print(f"Total was {cart_total}")
        print(f"discount was {discount}")
        print(f"New total is {new_total} ") 
        break   
    else:
        print("wrong input we dont have that now")      
