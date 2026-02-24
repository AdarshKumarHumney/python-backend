class Charater:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(f"{self.name} is walking")
class Enemy(Charater):
    def roar(self):
        print(f"{self.name} ROAR")
class Dragon(Enemy):
    def walk(self):
        print(f"{self.name} is flying")    
p1 = Dragon("Smaug")
p1.walk()                        