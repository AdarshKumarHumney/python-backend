class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def eat(self):
        print(f"{self.name} eats an apple health is restored")
        self.health+=10
    def attack(self, target):
        print(f"{self.name} attacks {target.name}")
        target.takeDamage(20)
class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 50
    def takeDamage(self, amount):
        self.health-= amount
        print(f"{self.name} took {amount} damage. Health is now {self.health}")
           
player1 = Hero("Adarsh")
player1.eat() 
print(f"The health of player1 is {player1.health}")
monster = Enemy("kutta")
player1.attack(monster)