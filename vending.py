import os
import json
import time
class VendingMachine:
    def __init__(self):
        self.inventory = {}
        workinglo1= os.path.dirname(__file__)
        filelo1 = os.path.join(workinglo1,"Vendin1.json")
        if "Vendin1.json" in os.listdir(workinglo1):
            with open(filelo1,"r") as g:
                self.inventory = json.load(g)    
        else:
            print("Hello!! Please add some items as the machine is empty")
    def printinventory(self):
        for i,details in self.inventory.items():
                print(f"{i}-- stock = {details['stock']} price = {details['price']}")                        
    def addinventory(self,name,price,stock):
        self.inventory[name]={'price':price,'stock':stock}
        print(f"{name} added successfully")
        self.savecart()
    def savecart(self):
        workingloc= os.path.dirname(__file__)
        fileloc = os.path.join(workingloc,"Vendin1.json")
        with open(fileloc,"w") as f:
            json.dump(self.inventory,f)
    def addtocart(self,item,userquantity):
        if item in self.inventory:
            if self.inventory[item]['stock']>=userquantity :
                print(f"{userquantity} of {item} added to the cart")
                return self.inventory[item]['price']*userquantity
            else:
                print(f"Sorry you want {userquantity} but we have only {self.inventory[item]['stock']}")
                print("To add the desired quantity continue") 
                return 0
        else:
            return 0      
    def pay(self,amount,money,listitems):
        if money>amount:
            print(f"You have given {money} and your change is {money-amount}")
            print("Thank you visit again")
            for i,quantity in listitems.items():
                self.inventory[i]['stock']-=quantity
                self.savecart()
            return True    
        elif money==amount:
            print("Thank you visit again")
            for i,quantity in listitems.items():
                self.inventory[i]['stock']-=quantity
                self.savecart()
            return True    
        else:
            print(f"The money that you are providing is less you need more{amount-money}")
            return False
print("Welcome to vending machine")
v1 = VendingMachine()
while True:
    v1.printinventory()
    total=0
    cart={}
    print("Menu-- press\n Add-- for add new items in cart\n Sale-- for making the purchase\n Exit")        
    userinput = input("What do you want to do")
    time.sleep(2)
    if userinput.lower()=="add":
        name1 = input("Input the product that you wanted to add")
        try:
            stock1 = int(input("Input the number of quantity you wanted to add"))
            price1 = int(input("input the amount of the product"))
        except ValueError:
            print("Please enter in numerical value")    
            continue
        v1.addinventory(name1,price1,stock1)
        time.sleep(2)
        continue
    elif userinput.lower()=="exit":
        print("User is exiting")
        break
    elif userinput.lower()=="sale":
        while True:
            userbuy=input("Input the product that you wanted to buy")
            userquantity = int(input("How many items do you wanted to buy"))
            time.sleep(2)
            current_itemcost = v1.addtocart(userbuy,userquantity)
            if current_itemcost>0: 
                total+= current_itemcost
                cart[userbuy]=userquantity
                userchoice = input("Do you want to buy more or do you want to pay")
                if userchoice.lower()=="buy":
                    continue
                else:
                    time.sleep(2)
                    while True:
                        print(f"Your total bill amount is {total}")
                        money = int(input("Input the amount of money that you have"))
                        if v1.pay(total,money,cart):
                            break
                        else:
                            usermoney = input("Do you have the extra money")
                            if usermoney.lower()=="yes":
                                continue
                            else:
                                print("Sorry cannot make the transaction")
                                break
                    break
            else:
                break
    else:
        print("Please enter the correct input")    
        continue  

