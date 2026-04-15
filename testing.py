def validateName(name):
    allowed ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 - "
    try:
        value = float(name)
        return {"success":False,"message":f"{value} has to be a string"}
    except ValueError:
        value = name
        for char in value:
            if char not in allowed:
                return {"success":False,"message":f"{char} is not allowed in the name"}    
        if 3<=len(value)<20:
            return {"success":True,"message":f"{value} is passed as the name"}
        else:
            return {"success":False,"message":f"{value} is not in the range of allowed limit"}
def validatePrice(price):
    
    try:
        value = float(price)
        if 0<len(str(price))<10:
            return {"success":True,"message":f"{value} is passed as price"}
        else:
            return {"success":False,"message":f"{value} is way too long please shorten the price"}
    except ValueError:
        return {"success":False,"message":f"{price} cannot be a string"}
def validateStock(stock):
    try:
        value = int(stock)
        if 0<len(str(stock))<4:
            return {"success":True,"message":f"{value} is passed as stock"}
        else:
            return {"success":False,"message":f"{value} is way to much to hold in a vending machine"}
    except ValueError:
        return {"success":False,"message":f"{stock} cannot be accepted as the stock value"}
report_value ={}
'''method1 = {"name":input("Enter the name of the product").strip(),
              "price":input("Enter the price of the product").strip(),
              "stock":input("Enter the stock value of the prodcut").strip()}'''
input_dict = {"name": "Chocolate", "price": 1.00}
function_dict = {"name":validateName,
                 "price":validatePrice,
                 "stock":validateStock}
for data,func in function_dict.items():
    user_input = input_dict.get(data)
    if user_input==None or user_input=="":
        report_value[data]="This field is required and cannot be empty"
        continue
    report = func(user_input)
    if not report['success']:
        report_value[data]=report['message']
if not report_value:
    print("Product added successfully")
else:
    print("Product was not added because")
    print(report_value)
