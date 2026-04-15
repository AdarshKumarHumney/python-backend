import random
class Character:
    def __init__(self,name,health):
        self.name = name
        self.health= health
    def take_damage(self,amount):
        self.health-=amount
        print(f"{self.name} took {amount} damage")
class Hero(Character):
    def attack(self, target):
        damage = int(input("How much damage do you wnant to inflict"))
        target.take_damage(damage)        
class Enemy(Character):
    def attack(self,target):
        damage = random.randint(5,15)
        target.take_damage(damage)
p1 = Hero("Superman",100)
e1 = Enemy("Darkseid",100)
while p1.health>=0 or e1.health>=0:
    p1.attack(e1)
    if e1.health == 0 or e1.health<0:
        e1.health =0
        print(f"You won...{e1.name} died")
        break
    e1.attack(p1)
    if p1.health==0 or p1.health<0:
        p1.health=0
        print(f"You lost...{p1.name} died")
        break        