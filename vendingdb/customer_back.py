class Customer:
    def __init__(self,connect):
        self.connect = connect
    def showStock(self):
        prod = []
        value = self.connect.showInventory()
        if value['data']:
            prod_tag = ["id","name","price","stock"]
            for i in value['data']:
                if i[3]>0:
                    prod.append(dict(zip(prod_tag,i)))
            return {"success":True,"message":"Here are the list of products","data":prod}
        else:
            return {"success":False,"message":value['message'],"data":None}
    def searchIdStock(self,id):
        value = self.connect.searchId(id)
        return value
    def buy(self,id):
        value = self.connect.updateBuy(id)
        return value