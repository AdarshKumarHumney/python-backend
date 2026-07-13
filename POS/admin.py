class Admin:
    def __init__(self,admin_manager,inventory,security):
        self.am = admin_manager
        self.im = inventory
        self.s1 = security
        self.admin_menu={"print":self.printAdmin,
            "search":self.searchAdmin,
            "update":self.updateAdmin,
            "delete":self.deleteAdmin,
            "exit":self.exitAdmin}
    def signUp(self):
        print("You are a new user please enter your credentials")
        return self.addAdmin()
    def signIn(self):
        print("Welcome to Admin-Menu page")
        print("Please enter your credentials")
        count = 3
        allow = False
        while count>0:
            email = input("Please input the mail")
            password = input("Please input the password")
            response = self.s1.authenticate_admin(email,password)
            if response['data']:
                print("Admin authenticated.")
                allow = True
                break
            else:
                print(response['message'])
                count-=1
                continue
        return allow
    def addAdmin(self):
        name = input("Enter your name")
        while True:
            mail = input("Enter your mail")
            search_response = self.am.searchEmail(mail)
            if search_response['data']:
                print("Please enter a new email this email is already in the use")
                continue
            else:
                break
        password= input("Enter your password")
        response = self.am.addAdmin(name,mail,password)
        if response['value']:
            print("admin added to the table successfully")
        else:
            print(f"There was a problem adding the admin - {response['message']}")
        return True
    def printAdmin(self):
        response = self.am.printList()
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
    def searchAdmin(self):
        mail = input("Enter the mail you want to search")
        response = self.am.searchEmail(mail)
        if not response['value']:
            print("There was problem in the database")
            return True
        if response['data']:
            print(f"Here is the admin - {response['data']}")
        else:
            print(f"There is no admin with the email - {mail}")
        return True
    def updateAdmin(self):
        self.printAdmin()
        while True:
            try:
                id = int(input("Enter the id from the list that you want to update"))
                break
            except ValueError:
                print("Please enter the id in digits format")
        while True:
            response_search = self.am.searchId(id)
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
                response = self.am.updateName(id,name)
                if response['value']:
                    print("Update successfull")
                else:
                    print(f"There was a problem in updating the name- {response['message']}")
                break
            elif options=="email":
                email = input("Please give a new email for update")
                response_search = self.am.searchEmail(email)
                if response_search['data']:
                    print("Email already present please provide with the new email")
                    continue
                response = self.am.updateEmail(id,email)
                if response['value']:
                    print("Email updated successfully")
                else:
                    print(f"There was a problem {response['message']}")
                break
            elif options=="password":
                password = input("Please input new password")
                response = self.am.updatePassword(id,password)
                if response['value']:
                    print("Password updated successfully")
                else:
                    print(f"There was a problem - {response['message']}")
                break
            else:
                print("Please select from the above list")
        return True
    def deleteAdmin(self):
        self.printAdmin()
        while True:
            while True:
                try:
                    id = int(input("Please select the id from the above that you want to delete"))
                    break
                except ValueError:
                    print("Please provide the id in digits")
            response_search = self.am.searchId(id)
            if not response_search['value']:
                print("There was problem in the database")
                break
            if not response_search['data']:
                print(f"Wrong id selected.")
                continue
            print(f"Here is the data - {response_search['data']}")
            confirm = input("Do you really want to delete the data?").lower()
            if confirm=="yes":
                response = self.am.deleteAdmin(id)
                if response['value']:
                    print(f"{id} was deleted successfully")
                else:
                    print(f"There was problem deleting the id - {response['message']}")
            else:
                print("Id deleted operation cancel")
            break
        return True
    def exitAdmin(self):
        print("Exiting the admin menu")
        return False
    def run(self):
        create = False
        while True:
            print("---Welcome to Admin Menu---")
            select= input("Please select signIn/SignUp or exit to continue").lower()
            if select == "signup":
                response = self.signUp()
            elif select == "signin":
                response = self.am.printList()
                if response['data']:
                    create = self.signIn()
                    if create:
                        break
                    else:
                        print("There was problem in login with your credentials")
                else:
                    print("There are no admins at the moment please signup first")
                    continue
            elif select == "exit":
                break
            else:
                print("Please select from the above set of above choices")
        while create:
            select = input(" | ".join(self.admin_menu.keys()).upper()).lower()
            if select in self.admin_menu:
                response = self.admin_menu[select]()
                if not response:
                    print("Exiting from the admin menu")
                    break
            else:
                print("Please select from the above set of menu")
        inventory_menu = {"add": self.im.addItem,
                        "print": self.im.printList,
                        "search": self.im.search,
                        "update": self.im.update,
                        "delete": self.im.delete,
                        "exit": None}
        while True:
            inventory_choice = input("Do you want to enter the inventory menu? YES | NO").strip().lower()
            if inventory_choice == "yes":
                print("-------INVENTORY MENU-------")
                choice = input("Please login || exit to enter the menu").strip().lower()
                if choice == "login":
                    allow = self.signIn()
                    if not allow:
                        print("Login credentials did not matched.")
                        continue
                    while True:
                        print("----WELCOME TO INVENTORY MENU-----")
                        select = input(" | ".join(inventory_menu.keys()).upper()).lower()
                        if select == "exit":
                            print("Exiting from the inventory menu")
                            break
                        elif select in inventory_menu:
                            response = inventory_menu[select]()
                            continue
                        else:
                            print("Please select from the above set of choices")
                        continue
                elif choice == "exit":
                    print("Exiting from the inventory menu")
                    break
                else:
                    print("Please select from the above set of choices")
            elif inventory_choice == "no":
                print("closing...")
                break
            else:
                print("Please select from the above set of choices")
        self.am.closeDb()
