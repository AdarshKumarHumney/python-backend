class User:
    def __init__(self,user_manager,security,inventory,admin):
        self.um = user_manager
        self.sec = security(admin,user_manager)
        self.im = inventory
    def signUp(self):
        print("Welcome new user... please enter your credentials")
        return self.addUser()
    def signIn(self):
        print("Admin Signin")
        print("Please enter your credentials")
        count = 3
        allow = False
        while count>0:
            email = input("Please input the mail")
            password = input("Please input the password")
            response = self.s1.authenticate_user(email,password)
            if response['data']:
                print("Admin authenticated.")
                allow = True
                break
            else:
                print(response['message'])
                count-=1
                continue
        return allow
    def addUser(self):
        name = input("Enter your name")
        while True:
            mail = input("Enter your mail")
            search_response = self.um.searchEmail(mail)
            if search_response['data']:
                print("Please enter a new email this email is already in the use")
                continue
            else:
                break
        password= input("Enter your password")
        response = self.um.addUser(name,mail,password)
        if response['value']:
            print("admin added to the table successfully")
        else:
            print(f"There was a problem adding the admin - {response['message']}")
        return True
    def printUSer(self):
        response = self.um.printUSer()
        if response['value']:
            if response['data']:
                print("Here are the list of the admin")
                for i in response['data']:
                    print(i)
            else:
                print("There are no admins at the moment")
        else:
            print(f"There was a problem {response['message']}")
        return True
    def searchUser(self):
        mail = input("Enter the mail you want to search")
        response = self.um.searchEmail(mail)
        if not response['value']:
            print("There was problem in the database")
            return True
        if response['data']:
            print(f"Here is the admin - {response['data']}")
        else:
            print(f"There is no admin with the email - {mail}")
        return True
    def updateUSer(self):
        self.printUSer()
        while True:
            try:
                id = int(input("Enter the id from the list that you want to update"))
                break
            except ValueError:
                print("Please enter the id in digits format")
        while True:
            response_search = self.um.searchId(id)
            if not response_search['value']:
                print("There was problem in the database")
                break
            if not response_search['data']:
                print("Id not found.")
                break
            print(f"Id found- {response_search['data']}")
            options = input("What do you want to update- NAME||EMAIL||PASSWORD").lower()
            if options == "name":
                name = input("Please type in the new name")
                response = self.um.updateName(id,name)
                if response['value']:
                    print("Update successfull")
                else:
                    print(f"There was a problem in updating the name- {response['message']}")
                break
            elif options=="email":
                email = input("Please give a new email for update")
                response_search = self.um.searchEmail(email)
                if response_search['data']:
                    print("Email already present please provide with the new email")
                    continue
                response = self.um.updateEmail(id,email)
                if response['value']:
                    print("Email updated successfully")
                else:
                    print(f"There was a problem {response['message']}")
                break
            elif options=="password":
                password = input("Please input new password")
                response = self.um.updatePassword(id,password)
                if response['value']:
                    print("Password updated successfully")
                else:
                    print(f"There was a problem - {response['message']}")
                break
            else:
                print("Please select from the above list")
        return True
    def deleteUser(self):
        self.printUSer()
        while True:
            while True:
                try:
                    id = int(input("Please select the id from the above that you want to delete"))
                    break
                except ValueError:
                    print("Please provide the id in digits")
            response_search = self.um.searchId(id)
            if not response_search['value']:
                print("There was problem in the database")
                break
            if not response_search['data']:
                print(f"Wrong id selected.")
                continue
            print(f"Here is the data - {response_search['data']}")
            confirm = input("Do you really want to delete the data?").lower()
            if confirm=="yes":
                response = self.um.deleteUser(id)
                if response['value']:
                    print(f"{id} was deleted successfully")
                else:
                    print(f"There was problem deleting the id - {response['message']}")
            else:
                print("Id deleted operation cancel")
            break
        return True
    def exitUser(self):
        print("Exiting the User menu")
        return False
    def run(self):
        create = False
                self.um.closeDb()
