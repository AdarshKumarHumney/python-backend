import os
import sqlite3
class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.make_db()
    def make_db(self):
        filelocation = os.path.dirname(__file__)
        new_dir = "testdb"
        new_db = "new_db.db"
        full_dir = os.path.join(filelocation,new_dir)
        os.makedirs(full_dir,exist_ok=True)
        try:
            full_db = os.path.join(full_dir,new_db)
            self.connection = sqlite3.connect(full_db)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(e)
        self.CreateAdminTable()
        self.CreateUserTable()    
    def CreateAdminTable(self):
        create_table_querry = '''CREATE TABLE IF NOT EXISTS admin(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL);'''
        self.cursor.execute(create_table_querry)
        self.connection.commit()
    def CreateUserTable(self):
        create_table_querry = '''CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER NOT NULL);'''
        self.cursor.execute(create_table_querry)
        self.connection.commit()
    def InserIntoAdmin(self,name,email,password):
        insert_querry_admin = "INSERT INTO admin(name, email, password) VALUES (?,?,?)" 
        try:
            self.cursor.execute(insert_querry_admin,(name,email,password,))
            self.connection.commit()
            print("value into admin was added successfully")
        except sqlite3.Error as e:
            print(e)
    def InsertIntoUser(self,name,email,age):
        inser_querry_user = "INSERT INTO user(name,email,age) VALUES (?,?,?)"
        try:
            self.cursor.execute(inser_querry_user,(name,email,age,))
            self.connection.commit()
            return {"value":True,"message":"Successfully entered into User"}
        except sqlite3.Error as e:
            return{"value":False,"message":e}
    def searchDataBase(self,table,field,value):
        search_table_querry = f"SELECT * FROM {table} WHERE {field} = ?"
        self.cursor.execute(search_table_querry,(value,))
        return self.cursor.fetchall()
    def PrintTable(self,choice):
        all_querry = f"SELECT * FROM {choice}"
        self.cursor.execute(all_querry)
        list_user = self.cursor.fetchall()
        return list_user
    def UpdateDatabase(self,table,field,field_value,id_value):
        update_table_querry = f"UPDATE {table} SET {field}=? WHERE id=?"
        try:
            self.cursor.execute(update_table_querry,(field_value,id_value,))
            self.connection.commit()
            return {"value" : True, "message":"Updated Successfully" }
        except sqlite3.Error as e:
            return {"value":False,"message":e}
    def DeleteDatabase(self,table,id):
        delete_database = f"DELETE FROM {table} WHERE id=?"
        try:
            self.cursor.execute(delete_database,(id,))
            self.connection.commit()
            return{"value": True, "message":"Successfully deleted"}
        except sqlite3.Error as e:
            return{"value":False,"message":e}
    def SecurityCheck(self,table,field1,field2,value1,value2):
        search_querry = f"SELECT * FROM {table} WHERE {field1}=? AND {field2}=?"
        try:
            self.cursor.execute(search_querry,(value1,value2,))
            got_result = self.cursor.fetchone()
            return got_result
        except sqlite3.Error:
            return False
class People:
    def __init__(self,database):
        self.database = database
    def ConvertToDic(self,list1,rows):
        result = []
        for i in list1:
            convert = dict(zip(rows,i))
            result.append(convert)
        return result
    def SearchTable(self,table,field,value,colums):
        search_list = self.database.searchDataBase(table,field,value)
        return self.ConvertToDic(search_list,colums)
    def printUser(self,choice):
        found_list = self.database.PrintTable(choice)
        return found_list
    def UpdateTable(self,table,field,field_value,id_value):
        return self.database.UpdateDatabase(table,field,field_value,id_value)
    def DeleteTable(self,table,id):
        return self.database.DeleteDatabase(table,id)
class AdminUser(People):
    def __init__(self, database):
        super().__init__(database)
        self.rows = ["id","name","email","password"]
        self.table = "admin"
    def AddAdmin(self,name,email,password):
        self.database.InserIntoAdmin(name,email,password)
    def SearchAdmin(self,choice,value):
        return super().SearchTable(self.table,choice,value,self.rows)
    def PrintList(self):
        return super().ConvertToDic(super().printUser(self.table),self.rows)
    def UpdateAdmin(self,field,field_value,id_value):
        return super().UpdateTable(self.table,field,field_value,id_value)
    def DeleteAdmin(self,id):
        return super().DeleteTable(self.table,id)
class Security:
    def __init__(self,connected):
        self.connected = connected
        self.login = False
    def LoginCheck(self,table,email,password):
        result_found = self.connected.SecurityCheck(table,"email","password",email,password)
        if result_found:
            self.login = True
            return {"login":self.login,"message":"login credentials matched"}
        else:
            return {"login":self.login,"message":"login did no matched"}
class NormalUser(People):
    def __init__(self, database):
        super().__init__(database)
        self.table = "user"
        self.rows = ["id","name","email","age"]
    def InsertUser(self,name,email,age):
        return self.database.InsertIntoUser(name,email,age)
    def SearchUser(self,choice,value):
        return super().SearchTable(self.table,choice,value,self.rows)
    def UpdateUser(self,field,field_value,id_value):
        return super().UpdateTable(self.table,field,field_value,id_value)
    def PrintList(self):
        return self.ConvertToDic(super().printUser(self.table),self.rows)
    def DeleteUser(self,id):
        return super().DeleteTable(self.table,id)
print("Welcome to Db with class")
d1 = Database() 
a1 = AdminUser(d1)
s1 = Security(d1)
u1 = NormalUser(d1)
admin_check = "12345"
allowed = False
counter= 3
def print_list(choice):
        user_list = choice.PrintList()
        for i in user_list:
            print(i)
while counter>0:
    Admin_pass = input("Please input the admin password")
    if Admin_pass == admin_check:
        print("Creditials matched successfully")
        allowed = True
        break
    else:
        counter-=1
        print(f"You have {counter} chances left")
try:
    if allowed:
        while True:
            select = input("Do you want to add||search||print||update||delete||exit")
            if select.lower()=="add":
                userchoice = input("Do you want to add a admin yes/no")
                if userchoice.lower() == "yes":
                    admin_name = input("Please input the name of your admin")
                    admin_email = input("Please input the mail of your admin")
                    admin_password = input("Please input the password")
                    try:
                        a1.AddAdmin(admin_name,admin_email,admin_password)
                        print("Admin addedd successfully")
                    except sqlite3.Error as e:
                        print(e)
                elif userchoice.lower() == "no":
                    print("Thank you")
                    break
                else:
                    print("please select either yes or no")
                continue
            elif select.lower()=="search":
                choice = input("Search Admin by-- Id||Name||Email")
                if choice.lower()=="id":
                    while True:
                        while True:
                            try:
                                value = int(input("Please provide an id to search for"))
                                break
                            except ValueError:
                                print("Please give a digit as input")
                                continue
                        id_found = a1.SearchAdmin(choice,value)
                        if id_found:
                            for i in id_found:
                                print(i)
                            break
                        else:
                            print(f"{value} is not in the database")
                            exit_choice = input("Do you want to search again or exit")
                            if exit_choice.lower()=="exit":
                                break
                            else:
                                continue
                elif choice.lower()=="name":
                    while True:
                        value = input("Please provide a name for search in Admin")
                        name_found = a1.SearchAdmin(choice,value)
                        if name_found:
                            for i in name_found:
                                print(i)
                            break
                        else:
                            print(f"{value} is not in the database")
                            exit_choice = input("Do you want to search again or exit")
                            if exit_choice.lower()=="exit":
                                break
                            else:
                                continue
                elif choice.lower()=="email":
                    while True:
                        value = input("Please give an email to search")
                        email_found = a1.SearchAdmin(choice,value)
                        if email_found:
                            for i in email_found:
                                print(i)
                            break
                        else:
                            print(f"{value} is not in the database")
                            exit_choice = input("Do you want to search again or exit")
                            if exit_choice.lower()=="exit":
                                break
                            else:
                                continue
                else:
                    print("Please select from the above set of choices")
                continue
            elif select.lower()=="print":
                print_list(a1)
                continue
            elif select.lower()=="update":
                while True:
                    update_choice = input("Do you wish to continue or exit")
                    if update_choice.lower()=="yes":
                        print("Here are the list of user that we have")
                        print_list(a1)
                        while True:
                            try:
                                id_value = int(input("Select the id of  the user you want to update"))
                                break
                            except ValueError:
                                print("Please select the id in digits")
                                continue
                        search_result = a1.SearchAdmin("id",id_value)
                        if search_result:
                            field = input("DO you wan to update name||email||password")
                            if field.lower()=="name":
                                field_value = input("Please select the updated name")
                                update_result = a1.UpdateAdmin(field,field_value,id_value)
                                if update_result['value']:
                                    print(update_result['message'])
                                    break
                                else:
                                    print(update_result['message'])
                                continue
                            elif field.lower()=="email":
                                while True:
                                    field_value = input("Please select the updated email that you want")
                                    search_mail= a1.SearchAdmin("email",field_value)
                                    if search_mail:
                                        print("Mail is already present in the database please use something else")
                                        continue
                                    else:
                                        break
                                update_result = a1.UpdateAdmin(field,field_value,id_value)
                                if update_result:
                                    print(update_result['message'])
                                    break
                                else:
                                    print(update_result['message'])
                                continue
                            elif field.lower()=="password":
                                field_value=input("Please select the new password that you want to update")
                                update_result = a1.UpdateAdmin(field,field_value,id_value)
                                if update_result:
                                    print(update_result['message'])
                                    break
                                else:
                                    print(update_result['message'])
                                continue
                            else:
                                print("Please select from the choices ubove")
                                continue
                        else:
                            print("The id that you search was not in the database")
                            continue
                    elif update_choice.lower()=="exit":
                        break
                    else:
                        print("please select from the above set of choices")
                        continue
            elif select.lower()=="delete":
                print("Here are the list of amin user")
                print_list(a1)
                while True:
                    while True:
                        try:
                            delete_id = int(input("Please select id from the above list"))
                            break
                        except ValueError:
                            print("Please select the id in digits")
                            continue
                    search_id = a1.SearchAdmin("id",delete_id)
                    if search_id:
                            print(search_id)
                            delete_choice = input("Are you sure you want to delete the above id")
                            if delete_choice.lower()=="yes":
                                delete_result = a1.DeleteAdmin(delete_id)
                                if delete_result['value']:
                                    print(delete_result['message'])
                                    break
                                else:
                                    print(delete_result['message'])
                                    break
                            else:
                                print("not deleting the id")
                                break
                    else:
                        print("Id no the list, please select the id from the above list")
            elif select.lower()=="exit":
                print("Do come again")
                break
            else:
                print("Please select from the above set of choices")
    else:
        print("You enterd the password incorrectly 3 times")
        print("See you again")
    counter=3
    Allow_login=False
    while True:
        input_choice= input("Do you want to login")
        if input_choice.lower()=="yes":      
            while counter>0:
                Admin_email = input("Please input your admin email id")
                Admin_password = input("Please input your password")
                Result=s1.LoginCheck("admin",Admin_email,Admin_password)
                if Result['login']:
                    Allow_login=Result['login']
                    print(Result['message'])
                    break
                else:
                    counter-=1
                    print(Result['message'])
                    print(f"You have{counter} chances left")
                    continue
            break
        else:
            print("You left the database")
            break
    if Allow_login:
        print("Welcome to User database")
        while True:
            user_choice = input("Add||Update||Search||Print||Delete||Exit")
            if user_choice.lower()=="add":
                name= input("Please enter the name of user")
                email = input("Please enter the mail of user")
                found_mail = u1.SearchUser("email",email)
                if found_mail:
                    print("mail already in use please use some other email")
                    continue
                while True:
                    try:
                        age = int(input("Please enter the age of user"))
                        break
                    except ValueError:
                        print("Please enter the age in numerical value")
                        continue
                value_return = u1.InsertUser(name,email,age)
                if value_return['value']:
                    print(value_return['message'])
                else:
                    print(value_return['message'])
                continue
            elif user_choice.lower()=="search":
                while True:
                    search_choice = input("Search by Id||Name||Email||age")
                    if search_choice.lower()=="id":
                        while True:
                            try:
                                id_value = int(input("Please input the id that you want to search"))
                                break
                            except ValueError:
                                print("Please input the value in digits")
                                continue
                        search_value = u1.SearchUser(search_choice,id_value)
                        if search_value:
                            for i in search_value:
                                print(i)
                            break
                        else:
                            print(f"{id_value} in not in the database")
                            search_again = input("Do you want to search another id")
                            if search_again.lower()=="yes":
                                continue
                            else:
                                break
                    elif search_choice.lower()=="name":
                        name_value = input("Please input the name that you want to search")
                        name_found = u1.SearchUser(search_choice,name_value)
                        if name_found:
                            for i in name_found:
                                print(i)
                            break
                        else:
                            print(f"{name_value} is not in the database")
                            search_again = input("Do you want to search again")
                            if search_again.lower()=="yes":
                                continue
                            else:
                                break
                    elif search_choice.lower()=="email":
                        email_value = input("Please input mail that you want to search")
                        mail_found = u1.SearchUser(search_choice,email_value)
                        if mail_found:
                            for i in mail_found:
                                print(i)
                            break
                        else:
                            print(f"{email_value} was not in the database")
                            search_again = input("Do you want to search again")
                            if search_again.lower()=="yes":
                                continue
                            else:
                                break
                    elif search_choice.lower()=="age":
                        while True:
                            try:
                                age_value = int(input("Please select the age that you want to search"))
                                break
                            except ValueError:
                                print("Please input value in digits")
                                continue
                        age_found = u1.SearchUser(search_choice,age_value)
                        if age_found:
                            for i in age_found:
                                print(i)
                            break
                        else:
                            print(f"No user with age{age_value} in the database")
                            search_again = input("Do you want to search again")
                            if search_again.lower()=="yes":
                                continue
                            else:
                                break
                    else:
                        print(f"{search_choice} is not in the above list")
                        continue
            elif user_choice.lower()=="update":
                print("Here are the list of user in the database")
                print_list(u1)
                while True:
                    try:
                        update_id = int(input("Please input the id that you want to update"))
                        break
                    except ValueError:
                        print("Please select the id in numerical value")
                        continue
                search_id = u1.SearchUser("id",update_id)
                if search_id:
                    update_choice = input("Update Name||Email||Age")
                    if update_choice.lower()=="name":
                        update_name = input("Please input the name that you want to update")
                        update_result = u1.UpdateUser(update_choice,update_name,update_id)
                        if update_result['value']:
                            print(update_result['message'])
                        else:
                            print(update_result['message'])
                    elif update_choice.lower()=="email":
                        update_mail = input("Please input the new mail")
                        search_mail = u1.SearchUser("email",update_mail)
                        if search_mail:
                            print("Email already present in the database please use another mail")
                            continue
                        else:
                            update_result = u1.UpdateUser(update_choice,update_mail,update_id)
                            if update_result['value']:
                                print(update_result['message'])
                            else:
                                print(update_result['message'])
                    elif update_choice.lower()=="age":
                        while True:
                            try:
                                update_age = int(input("Please input the new age"))
                                break
                            except ValueError:
                                print("Please input in digits")
                        update_result = u1.UpdateUser(update_choice,update_age,update_id)
                        if update_result['value']:
                            print(update_result['message'])
                        else:
                            print(update_result['message'])
                    else:
                        print(f"{update_choice} is not in the list")
                        continue
                else:
                    print(f"{update_id} is not in the list")
            elif user_choice.lower()=="print":
                print_list(u1)
                continue
            elif user_choice.lower()=="delete":
                print("Here are the list of user present in the database")
                print_list(u1)
                while True:
                    try:
                        delete_id = int(input("Select the id that you want to delete"))
                        break
                    except ValueError:
                        print("Please select the id in numerical value")
                        continue
                found_id = u1.SearchUser("id",delete_id)
                if found_id:
                    user_decision = input(f"Do you really want to delete {found_id[0]['name']} from the database")
                    if user_decision.lower()=="yes":
                        success = u1.DeleteUser(delete_id)
                        if success['value']:
                            print(success['message'])
                        else:
                            print(success['message'])
                    else:
                        print(f"Not deleting {found_id[0]['name']} from database")  
                    continue      
            elif user_choice.lower()=="exit":
                print("Getting out of user database")
                break
            else:
                print(f"{user_choice} is not in the list")
                continue    
    else:
        print("Admin Login failed")
    d1.connection.close()               
except sqlite3.Error as e:
     print(e)
