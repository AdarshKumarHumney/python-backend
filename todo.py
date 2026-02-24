import os
import json

class TaskManager:
    def __init__(self,usertask):
        self.task = usertask
    def addTask(self, task1):
        self.task.append(task1)    
        self.savefile()
    def showTask(self):
        print("The task are as follows")
        count =1
        for i in self.task:
            print(f"{count}: {i}")
            count+=1
    def deleteTask(self,task2):
        if task2 in self.task:
            self.task.remove(task2)
            self.savefile()
        else:
            print("you have entered wrong task")    
    def savefile(self):
        filedir = os.path.dirname(__file__)
        fileloc = os.path.join(filedir,"tasklist.json")
        with open(fileloc, "w") as f:
            json.dump(self.task,f)      
print("Welcome to to-do list")                         
filedir1 = os.path.dirname(__file__)
fileloc1 = os.path.join(filedir1,"tasklist.json")
if "tasklist.json" in os.listdir(filedir1):
    with open (fileloc1,"r") as g:
        new1 = json.load(g)
        newTask= TaskManager(new1)
        newTask.showTask()
else:
    newTask = TaskManager([])
while True:
    print("Do you want to do the following in the current list")
    print("Add/Delete/show/exit")
    userinput = input("What do yo want to do").lower()
    if userinput == "add":
        n1 = input("Please give a task to add")
        newTask.addTask(n1)
        continue
    elif userinput == "delete":
        n2 = input("Which task do you want to remove")
        newTask.deleteTask(n2)
        continue
    elif userinput == "show":
        newTask.showTask()
        continue
    elif userinput == "exit":
        print("i am here whenever you need me")
        break
    else:
        print("u input wrong choice")
