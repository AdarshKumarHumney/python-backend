inventory = [
    {"item": "Laptop", "price": 1200, "stock": 5},
    {"item": "Mouse", "price": 25, "stock": 50},
    {"item": "Monitor", "price": 300, "stock": 0},
    {"item": "Keyboard", "price": 100, "stock": 10}
]
total_stock = 0
out_of_stock=[]
total_inventory_cost=0
for i in inventory:
    print(f"We have {i['stock']} {i['item']}")
    total_stock+=i['stock']
    total_inventory_cost+=i['price']*i['stock']
    if i['stock']==0:
        out_of_stock.append(i['item'])
print(f"The total number of stock is {total_stock}")  
print(f"The total inventory cost is {total_inventory_cost}") 
for i in out_of_stock:
    print(f"The out of stock items are {i}")