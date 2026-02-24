class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        print(f"{self.name} is walking")
class Hero(Character):
    def heal(self):
        self.health+=10
        print(f"{self.name} walked and has a health now as{self.health}")
class Enemy(Character):
    def roar(self):
        print("ROAR")
p1 = Hero("Adarsh",100)
e1 = Enemy("Goblin",100)
e1.walk()
e1.roar()