Data = [
    {'Dish':"Burger",'price':100},
    {'Dish':'Pizza','price':250}
]
count = 0
print("What do you want to eat")
user_want = input("")
for i in Data:
    if user_want==i['Dish'] :
        print(f"The price is {i['price']}")
        count+=1
if count == 0:
    print("Item not on the menu")    
