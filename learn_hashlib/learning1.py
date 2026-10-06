from database import dataBase
import secrets
import hashlib
import hmac
class learn:
    def __init__(self):
        self.db = dataBase()
        self.status = self.createTable()
    def createTable(self):
        create = '''CREATE TABLE IF NOT EXISTS learn(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL UNIQUE,
        user_pass TEXT NOT NULL);'''
        response = self.db.runQuerry(create)
        return response
    def insertTable(self,name,passw):
        salt = secrets.token_hex(16)
        hash_byte = hashlib.pbkdf2_hmac("sha256",
                                        passw.encode("utf-8"),
                                        salt.encode("utf-8"),
                                        iterations=100_000,)
        hash_hex = hash_byte.hex()
        stored_token = f"{salt}:{hash_hex}"
        insert = "INSERT INTO learn(user_name,user_pass) VALUES (?,?)"
        insert_response = self.db.runQuerry(insert,(name,stored_token))
        return insert_response
    def returnPass(self,name):
        search = "SELECT * FROM learn WHERE user_name = ?"
        response_search = self.db.runQuerry(search,(name,))
        return response_search
    def matchPass(self,name,passw):
        find_pass = self.returnPass(name)
        if find_pass['data']==False:
            return False
        salt,passwStored = find_pass['data'][0]['user_pass'].split(":")
        print(f"salt - {salt}, password - {passwStored}")
        new_byte = hashlib.pbkdf2_hmac("sha256",
                                       passw.encode('utf-8'),
                                       salt.encode('utf-8'),
                                       iterations=100_000,)
        new_hex = new_byte.hex()
        print(f"new pass - {new_hex}")
        return hmac.compare_digest(passwStored,new_hex)
    def printList(self):
        printL = "SELECT * FROM learn"
        response = self.db.runQuerry(printL)
        if response['data']==[]:
            print("no user is present")
        else:
            print(response['data'])
l1 = learn()
if l1.status['value']==False:
    print("database problem, cannot continue")
else:
    while True:
        choice = input("Login/Signup/print/exit").lower().strip()
        if choice=="login":
            name = input("Enter your name")
            search = l1.returnPass(name)
            if search['data']==[]:
                print(f"No user is present with the name {name}")
                continue
            password = input("Enter your password")
            compare = l1.matchPass(name,password)
            if compare == True:
                print("Matched")
            else:
                print("Not the right password")
        elif choice=="signup":
            print("Welcome new user")
            while True:
                name = input("Please enter your name")
                search = l1.returnPass(name)
                if search['data']!= []:
                    print("name is already taken")
                    continue
                break
            password = input("Enter a password")
            response = l1.insertTable(name,password)
            if response['value']== True:
                print("User inserted successfully")
            else:
                print(f"Problem in adding user - {response['message']}")
        elif choice == "print":
            l1.printList()
        elif choice == "exit":
            print("Bye")
            break
        else:
            print("Please choose from the above set of choices")
        