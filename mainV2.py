import os
from database import Database
from security import Security
from model import AdminUser
from model import People
from model import NormalUser
from dotenv import load_dotenv
load_dotenv()
print("Welcome to Db with class")
db_name = os.getenv("DB_NAME")
d1 = Database(db_name) 
a1 = AdminUser(d1)
s1 = Security(d1)
u1 = NormalUser(d1)
p1 = People(d1)
admin_check = os.getenv("ADMIN_PASSWORD")
allowed = False
counter= 3
def PrintList(choice):
        user_list = choice.PrintList()
        for i in user_list:
            print(i)
        return True
def AddData(choice):
    user_choice = {}
    for field,convert in choice.REQUIRED_FIELDS.items():
        while True:
            try:
                val = input(f"Enter {field}. ").strip()
                user_choice[field]=convert(val)
                break
            except ValueError:
                print(f"Invalid input {field} must be a {convert.__name__}")
    response = choice.SaveUser(user_choice)
    print(response['message'])
    return True
def Search(choice):
    fields = choice.REQUIRED_FIELDS
    response = function_generate(fields)
    while True:
        print("What do you want to search for")
        print(response)
        user_choice = input().strip()
        if user_choice in fields:
            while True:
                try:
                    value = fields[user_choice](input(f"Enter {user_choice}."))
                    break
                except ValueError:
                    print(f"please input in{fields[user_choice].__name__}")
            search_result = choice.SearchUser(user_choice,value)
            if search_result['value']:
                print(search_result['message'])
                for j in search_result['data']:
                    print(j)
            else:
                print(search_result['message'])
            return True
        else:
            print("The field you search for is not in the database")
            exit_choice = input("Do you want to search again or exit? Yes/Exit").lower()
            if exit_choice=="yes":
                continue
            else:
                break
    return True
def Update(choice):
    print("Here are the list of users...")
    PrintList(choice)
    while True:
        try:
            update_id = int(input("Select the id you want to update"))
            break
        except ValueError:
            print("Please enter in digits")
            continue
    while True:
        search_result = choice.SearchUser("id",update_id)
        if not search_result['value']:
            print(search_result['message'])
            break
        print(search_result['message'])
        print(search_result['data'])
        fields = choice.REQUIRED_FIELDS
        print("What do you want to update")
        response = function_generate(fields)
        print(response)
        field_chose = input().lower().strip()
        if field_chose not in fields:
            print("The field you chose does not belong")
            exit_choice = input("press yes to continue update.. or press any other key to exit").lower()
            if exit_choice=="yes":
                continue
            else:
                break
        while True:
            try:
                field_value = fields[field_chose](input(f"Enter the new {field_chose}"))    
            except ValueError:
                print(f"Please input in {fields[field_chose].__name__} ")
                continue
            if field_chose=="email":
                email_search = choice.SearchUser(field_chose,field_value)
                if email_search['value']:
                    print("Please select another mail this one is already in database")     
                    continue    
            break
        update_result = choice.UpdateUser(field_chose,field_value,update_id)
        if update_result['value']:
            print(update_result['message'])
            break
        else:
            print(update_result['message'])
            break
    return True
def Delete(choice):
    print("Here are the list of user")
    PrintList(choice)
    while True:
        while True:
            try:
                delete_id= int(input("Select the id you want to delete"))
                break
            except ValueError:
                print("Please select id in didgits")
                continue
        search_result = choice.SearchUser("id",delete_id)
        if not search_result['value']:
            print(search_result['message'])
            break
        print(search_result['data'])
        while True:
            confirm = input("Do you really want to delete the above id? type Yes to delete it").lower().strip()
            if confirm!="yes":
                print("Not deleting from the database")
                break
            print("Deleting the id...")
            delete_confirm = choice.DeleteUser(delete_id)
            if delete_confirm['value']:
                print(delete_confirm['message'])
                break
            else:
                print(delete_confirm['message'])
                break
        break
    return True
def Exit(choice):
    select = input("Do you want to exit?Yes/no").lower()
    if select=="yes":
        return False
    else:
        return True
while counter>0:
    Admin_pass = input("Please input the admin password")
    if Admin_pass == admin_check:
        print("Creditials matched successfully")
        allowed = True
        break
    else:
        counter-=1
        print(f"You have {counter} chances left")
function_choice = {
    "add":AddData,
    "print":PrintList,
    "search":Search,
    "update":Update,
    "delete":Delete,
    "exit":Exit
}
def function_generate(choices):
    view = list(choices.keys())
    return " | ".join(view).upper()
def SystemRunner(user_object,choices_dict):
    print(f"--Welcome to {user_object.role} interface--")
    while True:
        choices = input(f"Select from {function_generate(choices_dict)}").lower()
        if choices in choices_dict:
            if not choices_dict[choices](user_object):
                break
        else:
            print(f"{choices} is not a valid command please select from the above")
if allowed:
    SystemRunner(a1,function_choice)
else:
    print("Admin password was not correct. login out of admin properties")
while True:
    admin_wants = input("Do you want to see user properties? Yes/No").lower().strip()
    if admin_wants=="yes":
        counter=3
        admin_login=False
        while counter>0:
            admin_email = input("Please enter your admin mail")
            admin_password = input("Please enter your password")
            allowed = s1.LoginCheck("admin",admin_email,admin_password)
            if allowed['login']:
                print(allowed['message'])
                admin_login = True
                break
            else:
                print(allowed['message'])
                counter-=1
                print(f"You have only {counter} chance left")
                continue
        if admin_login:
            SystemRunner(u1,function_choice)
        else:
            print("Admin credentials did not matched")
            break
        break
    elif admin_wants=="no":
        print("Login off")
        break
    else:
        print("Please select eithe yes or no")
        continue
p1.database.connection.close()
