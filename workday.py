class Workday:
    def __init__(self, delivery_count):
        self.delivery = delivery_count
    def calculate(self):
        if self.delivery<=20:
            netprice= self.delivery*50
        else:
            health_tax = (self.delivery-20)*10
            price = self.delivery*60
            netprice = price-health_tax
        print(f"you are actually earning {netprice}")

p1 = Workday(20)
p2 = Workday(25)
p3 = Workday(30)
p1.calculate()
p2.calculate()       
p3.calculate()
