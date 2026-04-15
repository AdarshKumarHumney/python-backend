import os
import json

class Workday:
    def __init__(self):
        # When we start, we need to figure out where the file is immediately
        self.currdire = os.path.dirname(__file__)
        self.filelocation = os.path.join(self.currdire, "userlist.json")
        
        # LOAD existing data immediately so we don't start empty!
        if os.path.exists(self.filelocation):
            with open(self.filelocation, "r") as f:
                self.listitems = json.load(f)
        else:
            self.listitems = []

    def save_to_history(self):
        with open(self.filelocation, "w") as f:
            json.dump(self.listitems, f, indent=4) # indent makes it readable

    def writelist(self, item):
        # FIX: Append (add to end) instead of replacing the whole list
        self.listitems.append(item)
        self.save_to_history()
        print(f"✅ Added '{item}' to the list.")

    def updatelist(self, updateitem):
        # FIX: used len() instead of length()
        if len(self.listitems) == 0:
            print("List is empty!")
        elif updateitem in self.listitems:
            self.listitems.remove(updateitem)
            self.save_to_history()
            print(f"❌ Removed '{updateitem}'")
        else:
            print("Item not found.")

# --- MAIN PROGRAM ---
p1 = Workday() # This now loads your old file automatically!

while True:
    print("\n--- MENU ---")
    userinput = input("Choose: Read, Update, Write, or Exit: ").lower()

    if userinput == "read":
        # We don't need to read the file again, p1.listitems already has the data!
        if len(p1.listitems) > 0:
            print("Here is your list:")
            for i in p1.listitems:
                print(f"- {i}")
        else:
            print("List is empty.")

    elif userinput == "write":
        userwant = input("What do you want to add? ")
        p1.writelist(userwant)

    elif userinput == "update":
        userupdate = input("What do you want to remove? ")
        p1.updatelist(userupdate)
    
    elif userinput == "exit":
        break
        
    else:
        print("Wrong entry")