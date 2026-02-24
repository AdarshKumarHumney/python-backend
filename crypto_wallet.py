import requests
import os
import json
class Portfolio:
    def __init__(self):
        self.assets={}
        self.loadWallet()
        self.print()
    def loadWallet(self):    
        fileLocation = os.path.dirname(__file__)
        scriptLocation= os.path.join(fileLocation,"crypto.json")
        if "crypto.json" in os.listdir(fileLocation):
            with open(scriptLocation,'r') as f:
                try:
                    values = json.load(f)
                    self.assets=values
                except json.JSONDecodeError:
                    print("Your json code was corrupted starting fresh")
                    self.sell_assets={}          
        else:
            print("File is not created add some crpyto")
    def print(self):
        if len(self.assets)==0:
            print("Your wallet is empty please add some crpto to read")
        else:
            for i in self.assets:
                print(f"you have {self.assets[i]} {i}")    
    def buy_asset(self,name,amount):
        if name in self.assets:
            self.assets[name]+=amount
            self.save()
            return{"message":f"You have successfully bought {amount} {name}"}
        else:
            self.assets[name]=amount
            self.save()
            return{"message":f"You have successfully bought {amount} {name}"}
    def sell_assets(self,name,amount):
        if name in self.assets:
            self.assets[name]-=amount
            self.save()
            return {"message":f"You have successfully sold {amount} {name}"}
        else:
            return {"message":f"you dont have {name} in your wallet"}
    def valueOfCurrentAsset(self,coin,currency):
        coin_value = self.value_of_coin(coin,currency)
        single_value = coin_value[coin]
        total = single_value*self.assets[coin]
        return{"total_value":total,"single_price":single_value}
    def value_of_coin(self,coin,currency):
        url = "https://api.coingecko.com/api/v3/simple/price"
        instructions = {'ids':coin,'vs_currencies':currency}
        try:
            response = requests.get(url,params=instructions,timeout=5)
            coin_value = response.json()
            value = coin_value[coin][currency]
            return {coin:value}
        except requests.exceptions.RequestException:
            print(f"there was a problem in connection")
            return {coin:0.0}
    def save(self):
        fileLocation = os.path.dirname(__file__)
        scriptLocation= os.path.join(fileLocation,"crypto.json")
        with open(scriptLocation,'w') as g:
            json.dump(self.assets,g)
w1 = Portfolio()
print("This is your personal crypto wallet")
while True:
    print("------Menu-------")
    print("press add to add crpto\n"
          "press sell to sell crypto\n"
          "press print to see what crypto do you hold\n"
          "press value to see the worth of your holdings\n"
          "press exit to exit the wallet")
    user_choice = input("What do you want to do")
    if user_choice.lower()=="add":
        user_coin = input("Which coin do you want to buy")
        try:
            user_amount = float(input("How much do you want to buy"))
        except ValueError:
            print("Please input a value in digits and not alphabets...")
            continue    
        read = w1.buy_asset(user_coin,user_amount)
        print(read['message'])
        continue
    elif user_choice.lower()=="sell":
        print("Here is the list of crypto that you hold")
        w1.print()
        user_choice1= input("Which coin do you want to sell")
        try:
            user_amount1 = float(input("How much you want to sell"))
        except ValueError:
            print("Please input a value in numbers and not alphabets...")  
            continue  
        read = w1.sell_assets(user_choice1,user_amount1)
        print(read['message'])
        continue
    elif user_choice.lower()=="print":
        w1.print()
        continue
    elif user_choice.lower()=="value":
        print("This the current holding of your wallet")
        w1.print()
        user_choice_value = input("Input the coin whose value you want to see")
        user_choice_currency = input("Please input for now in usd or inr")
        if user_choice_value in w1.assets:
            value_of_asset = w1.valueOfCurrentAsset(user_choice_value,user_choice_currency)
            print(f"The current {user_choice_value} in {user_choice_currency} is {value_of_asset['single_price']}")
            print(f"You are holding total of {w1.assets[user_choice_value]} of {user_choice_value}")
            print(f"Your total woth of {user_choice_value} in {user_choice_currency}is.....")
            user_holding = value_of_asset
            print(user_holding['total_value'])
        else:
            value1=w1.value_of_coin(user_choice_value,user_choice_currency)
            print(f"{user_choice_value} is not in your wallet but its current price is..")
            print(value1[user_choice_value])                                              
    elif user_choice.lower()=="exit":
        print("Have a great day!! Bye")
        break
    else:
        print(f"Your selection {user_choice} is not in the menu")
        continue