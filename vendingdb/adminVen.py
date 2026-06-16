class Admin:
    def __init__(self, database):
        self.connect = database
    def validateName(self,name):
        allowed ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 - "
        try:
            value = float(name)
            return {"success":False,"message":f"{value} has to be a string", "data":None}
        except ValueError:
            value = name
            for char in value:
                if char not in allowed:
                    return {"success":False,"message":f"{char} is not allowed in the name","data":None}    
            if 3<=len(value)<20:
                return {"success":True,"message":f"{value} is passed as the name","data":value}
            else:
                return {"success":False,"message":f"{value} is not in the range of allowed limit","data":None}
    def validatePrice(self,price):
        try:
            value = float(price)
            if 0<len(str(price))<10:
                return {"success":True,"message":f"{value} is passed as price", "data":value}
            else:
                return {"success":False,"message":f"{value} is way too long please shorten the price", "data":None}
        except ValueError:
            return {"success":False,"message":f"{price} cannot be a string", "data":None}
    def validateStock(self,stock):
        try:
            value = int(stock)
            if 0<=value<100:
                return {"success":True,"message":f"{value} is passed as stock", "data":value}
            else:
                return {"success":False,"message":f"{value} is way to much to hold in a vending machine", "data":None}
        except ValueError:
            return {"success":False,"message":f"{stock} cannot be accepted as the stock value", "data":None}
    def addStock(self,name,price,stock):
        return self.connect.addInventory(name,price,stock)
    def searchStock(self,name,price):
        return self.connect.searchInventory(name,price)
    def updateStock(self,name,price,stock):
        return self.connect.updateInventory(name,price,stock)
    def showStock(self):
        return self.connect.showInventory()
    def verify(self,name,price,stock):
        report_value ={}
        add_data = {}
        user_input_value = {"name":name,
                    "price":price,
                    "stock":stock}
        function_dict = {"name":self.validateName,
                        "price":self.validatePrice,
                        "stock":self.validateStock}
        for data,func in function_dict.items():
            user_input = user_input_value.get(data)
            if user_input==None or user_input=="":
                report_value[data]="This field is required and cannot be empty"
                continue
            report = func(user_input)
            if not report['success']:
                report_value[data]=report['message']
                continue
            add_data[data]=report['data']
        return (add_data,report_value)