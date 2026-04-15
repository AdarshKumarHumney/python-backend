def addtocart(self, item, userquantity):
    if item in self.inventory:
        if self.inventory[item]['stock'] >= userquantity:
            return {"Status": "Success",
                    "Total": self.inventory[item]['price'] * userquantity}
        else:
            return{"Status":"Fail", "Message":"Item out of stock"}
    else:
        return{"Status":"Fail","Message":"Item inputed incorrectly"}