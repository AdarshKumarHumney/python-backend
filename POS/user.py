class User:
    def __init__(self,user_manager,security,inventory,admin):
        self.um = user_manager
        self.sec = security
        self.im = inventory
        self.ad = admin
    def signUp(self):
        print("Welcome new user... please enter your credentials")
        return self.addUser()
    def signIn(self):
        print("User Signin")
        print("Please enter your credentials")
        count = 3
        while count>0:
            email = input("Please input the mail")
            password = input("Please input the password")
            response = self.sec.authenticate_user(email,password)
            if not response['value']:
                print("There is some problem in the database")
                break
            if response['data']:
                print("Admin authenticated.")
                allow = True
                return {"allow" : True, "data":response['data']}
            else:
                print(response['message'])
                count-=1
                continue
        return {"allow":False,"data":None}
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
        return response
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
        email = input("Enter the mail that you want to update")
        while True:
            response_search = self.um.searchEmail(email)
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
                response = self.um.updateName(email,name)
                if response['value']:
                    print("Update successfull")
                else:
                    print(f"There was a problem in updating the name- {response['message']}")
                break
            elif options=="email":
                mail = input("Please give a new email for update")
                response_search = self.um.searchEmail(mail)
                if response_search['data']:
                    print("Email already present please provide with the new email")
                    continue
                response = self.um.updateEmail(email,mail)
                if response['value']:
                    print("Email updated successfully")
                else:
                    print(f"There was a problem {response['message']}")
                break
            elif options=="password":
                password = input("Please input new password")
                response = self.um.updatePassword(email,password)
                if response['value']:
                    print("Password updated successfully")
                else:
                    print(f"There was a problem - {response['message']}")
                break
            else:
                print("Please select from the above list")
        return True
    def deleteUser(self):
        self.um.printUSer()
        while True:
            email = input("Please select the email from the above that you want to delete")
            response_search = self.um.searchEmail(email)
            if not response_search['value']:
                print("There was problem in the database")
                break
            if not response_search['data']:
                print(f"Wrong id selected.")
                continue
            print(f"Here is the data - {response_search['data']}")
            confirm = input("Do you really want to delete the data?").lower()
            if confirm=="yes":
                response = self.um.deleteUser(email)
                if response['value']:
                    print(f"{email} was deleted successfully")
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
        create= {"allow":False, "data":None}
        user_id = None
        print("Welcome to the app")
        while True:
            choice = input("SIGNIN || SIGNUP || EXIT").lower()
            if choice == "signin":
                create = self.signIn()
                if not create["allow"]:
                    print("Signin was unsuccessfull")
                    continue
                user_id = create['data']['user_id']
                break
            elif choice == "signup":
                response = self.signUp()
                if response['value']:
                    print("User signed up successfully")
                else:
                    print(f"There was problem in signin up.- {response['message']}")
            elif choice == "exit":
                print("Exiting..")
                break
            else:
                print("Please select from the above list of choice")
        while create['allow']:
            print("Here are the list of items that we have")
            response = self.im.printNamePrice()
            if not response['value']:
                print("There was some problem in the database to show the items")
                break
            if not response['data']:
                print("Currently we do not have any stock to show up")
                break
            for i in response['data']:
                print(f"Id-> {i['item_id']} || Name-> {i['item_name']} || Price-> {i['item_price']}")
            while True:
                print("...User Menu...")
                choice = input("BUY || UPDATE || DELETE || EXIT").lower()
                if choice == "buy":
                    check = self.um.showCart(user_id)
                    create_response = self.um.cartTable()
                    if not create_response['value']:
                        print(f"There was some problem in making cart - {create_response['message']}")
                        continue
                    if not check['value']:
                        print(f"There was some problem in the database hence the user data cannot be found - {check['message']}")
                        continue
                    if check['data']:
                        print("These are items that are in your cart")
                        for i in check['data']:
                                print(i)
                    else:
                        print("Lets fill your cart")
                    print("..Entering Cart Menu..")
                    while True:
                        buy_choice = input("ADD|| UPDATE || BUY || EXIT ").lower()
                        if buy_choice == "add":
                            while True:
                                try:
                                    item_id = int(input("Select the id of the item that you want to add"))
                                    break
                                except ValueError as e:
                                    print("Please input in integer")
                            check_item = self.im.searchById(item_id)
                            if not check_item['value']:
                                print(f"There is some problem in the database - {check_item['message']}")
                                continue
                            if not check_item['data']:
                                print("There are no items with the id that you have chosen please choose some other item and continue..")
                                continue
                            in_stock = check_item['data'][0]['item_quant']
                            if in_stock == 0:
                                print("The item that you selected is out of stock.. Please select another item")
                                continue
                            while True:
                                try:
                                    buy_quant = int(input("Please select the number of quantity you want to buy"))
                                    if buy_quant<=0:
                                        print("Quantity entered should be greater than 0")
                                        continue
                                    break
                                except ValueError as e:
                                    print(f"The quantity entered must be in integer - {e}")
                            cancelled = False
                            while buy_quant>in_stock:
                                print(f"We have - {in_stock} quantity in stock please choose the buy quantity respectively")
                                choose = input("1. Please decrease the quantity to proceed or || 2.select to cancle")
                                if choose == "1":
                                    while True:
                                        try:
                                            new_quant = int(input("Enter the new quantity"))
                                            if new_quant<=0:
                                                print("The quantity should be more than 0")
                                                continue
                                            break
                                        except ValueError as e:
                                            print("Please enter in integer")
                                    buy_quant = new_quant
                                elif choose == "2":
                                    print("Choose another product. thankyou")
                                    cancelled = True
                                    break
                                else:
                                    print("Please select from the above choice")
                            if cancelled:
                                break
                            cart = self.um.addToCart(user_id,item_id,buy_quant)    
                            if cart['value']:
                                print("Successfully added to the cart")
                            else:
                                print(f"There was some problem while adding to cart - {cart['message']}")
                        elif buy_choice == "update":
                            crashed = False
                            check = self.um.showCart(user_id)
                            if not check['value']:
                                print("There is problem with the database...")
                                continue
                            elif not check['data']:
                                print("There are no items in your cart to update..")
                                continue
                            else:
                                print("Here are list of items in your cart")
                                for i in check['data']:
                                    print(i)
                                while True:
                                    try:
                                        id_select = int(input("Select the item id that you want to update quantity of"))
                                        break
                                    except ValueError as e:
                                        print("Please select the id in integer only")
                                    search_item = self.um.searchCartId(id_select)
                                    if not search_item['value']:
                                        print("There is problem in the database")
                                        break
                                    if not search_item['data']:
                                        print("The id you provided does not have any item please select correct id")
                                        continue
                                    else:
                                        id = self.um.showItem(user_id,id_select)
                                        print(f"Here is your item - {id['data'][0]}")
                                        crashed = True
                                if not crashed:
                                    continue
                                stock = self.im.searchById(id_select)
                                while True:
                                    try:
                                        new_quant = int(input("Enter the modify quantity"))
                                        if new_quant<=0:
                                            print("PLease input the quantity more than 0")
                                            continue
                                        if new_quant>stock['data'][0]['item_quant']:
                                            print("new value cannot exceed stock stock.. Try again")
                                            continue
                                        else:
                                            break
                                    except ValueError as e:
                                        print("Input the stock value in integer")
                                update = self.um.updateCart(user_id,id_select,new_quant)
                                if not update['value']:
                                    print("Problem in the database")
                                    continue
                                else:
                                    print("Value updated successfully")
                        elif buy_choice == "buy":
                            create1 = self.um.createSaleTable()
                            create2 = self.um.createSaleItem()
                            if not create1['value'] or not create2['value']:
                                print("Problem in the database creating the sale table or saleitem table")
                                continue
                            total = 0
                            checkout = self.um.checkout(user_id)
                            if not checkout['value']:
                                print(checkout['message'])
                                continue
                            for i in checkout['data']:
                                print(i)
                                total = total+(i['item_quant']*i['item_price'])
                            sale = self.um.addToSale(user_id,total)
                            if not sale['value']:
                                self.um.db.rollbackTransaction()
                                print("There was problem in the database")
                                continue
                            sale_recipt = self.um.seeSale(user_id)
                            if not sale_recipt['value']:
                                print("Problem in getting sale recipt due to database")
                                continue
                            for i in checkout['data']:
                                item_add = self.um.addToSaleItem(sale['lastrowid'],i['item_id'],i['item_name'],i['item_quant'],i['item_price'])
                                if not item_add['value']:
                                    print(f"There was problem in adding - {i['item_name']}")
                                    self.um.db.rollbackTransaction()
                                    continue
                            sale_item = self.um.saleItem(sale['lastrowid'])
                            if not sale_item['value']:
                                print("there was some problem in the database")
                                self.um.db.rollbackTransaction()
                                continue
                            self.um.db.commitTransaction()
                            print("Here is your recipt")
                            for i in checkout['data']:
                                print(i)
                            for i in sale_item['data']:
                                print(i)
                        elif buy_choice == "exit":
                            print("Exiting from the buy menu")
                            break
                        else:
                            print("Please select form the above set of choices")
                elif choice == "update":
                    self.updateUSer()
                elif choice == "delete":
                    self.deleteUser()
                elif choice == "exit":
                    print("Exiting user app..")
                    create['allow'] = False
                    break
                else:
                    print("Please select from the above set of choices")
                    continue
