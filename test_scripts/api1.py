import requests
import time
base_url = "https://api.agify.io"
request1 = {}
while True:
    userchoice = input("To find the age with respect to your 1st name press start for exit press clear ")
    if userchoice.lower()=="start":
        userinput=input("Let's guess the age of yours just from your first name")
        request1['name']=userinput
        response = requests.get(base_url,params=request1)
        if response.status_code==200:
            print("Everything works fine")
            time.sleep(2)
            getresponse = response.json()
            print(getresponse)
            print(f"Your age according to {userinput} is {getresponse['age']}")
        else:
            print("There is something wrong please try again")
            continue    
    elif userchoice.lower()=="clear":
        print("Come again bye")
        break
    else:
        print("Please input either start/clear")    

