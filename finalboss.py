import os
import json
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 60
    def feed(self):
        if self.hunger<=0:
            print("he has eaten a lot, let him/her play")
        else:
            self.hunger-=10
            self.energy+=5
        self.save()    
    def play(self):
        if self.energy<=0:
            print("pet dose not have enough enery please feed it")
        else:    
            self.happiness+=10
            self.hunger+=5
            self.energy-=10 
            self.save()            
    def status(self):
        print(f"{self.name} || hunger = {self.hunger} || happiness = {self.happiness} || energy = {self.energy}")
    def save(self):
        data = {
            'name': self.name,
            'hunger': self.hunger,
            'happiness': self.happiness,
            'energy': self.energy
        }
        dirclocation1 = os.path.dirname(__file__)
        filelocation1 = os.path.join(dirclocation1,"pet_data.json")
        with open(filelocation1, "w")as g:
            json.dump(data,g)    
        print("Auto Saved")    
dirclocation = os.path.dirname(__file__)
filelocation = os.path.join(dirclocation,"pet_data.json")
if "pet_data.json"  in os.listdir(dirclocation):
    print("File found")
    with open(filelocation,"r") as f:
        loaddata = json.load(f)
        print(f"{loaddata}")
        New1 = loaddata['name']
        p1 = Pet(New1)
        p1.hunger = loaddata['hunger']
        p1.happiness = loaddata['happiness']
        p1.energy = loaddata['energy']
else:
    newpet = input("Name the pet")
    p1 = Pet(newpet)
    p1.save()
while True:
    p1.status()
    choice = input("Do you want to play or feed your pet or exit").lower()
    if choice == "feed":
        p1.feed()
    elif choice == "play":
        p1.play()
    elif choice == "exit":
        print("bye")
        break
    else:
        print("invalid choice")    
