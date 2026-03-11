import sqlite3
import os
def convertInDictionaryAdmin(list1):
    return {i[0]:{
        "email":i[1],
        "password":i[2]
    }for i in list1
    }
current_path = os.path.dirname(__file__)
dir_name = "database"
db_name = "newdb.db"
new_dir = os.path.join(current_path,dir_name)
os.makedirs(new_dir,exist_ok=True)
full_path = os.path.join(new_dir,db_name)
login_state = False
trial_pass = "12345"
counter = 3
try:
    connection = sqlite3.connect(full_path)
    cursor = connection.cursor()
    print("Database initialised successfully")
    create_admin = '''
    CREATE TABLE IF NOT EXISTS admin
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    );
    '''
    create_user = '''
    CREATE TABLE IF NOT EXISTS user
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER);
    '''
    cursor.execute(create_admin)
    connection.commit()
    while True:
        choice1 = input("Do you want to see the admin menu... YES/NO")
        if choice1.lower() == "yes":
            print("-----Admin Menu-----")
            pass_check = input("Please input the admin password to view admin menu")
            if pass_check == trial_pass:
                while True:
                    admin_choice = input("1. Enter the data\n""2. view admins\n""3. Exit\n")
                    if admin_choice == "1":
                        admin_email = input("Enter your email as username")
                        admin_password = input("Enter a strong password")
                        search_db = "SELECT * FROM admin WHERE email =?"
                        cursor.execute(search_db,(admin_email,))
                        result1 = cursor.fetchone()
                        if result1:
                            print("The username is already in the database please use different email")
                            continue
                        else:
                            insert_admin = "INSERT INTO admin (email, password) VALUES (?,?)"
                            cursor.execute(insert_admin,(admin_email,admin_password,))
                            connection.commit()
                            continue
                    elif admin_choice =="2":
                        view_query = "SELECT * FROM admin"
                        cursor.execute(view_query)
                        admin_list = cursor.fetchall()
                        admin_dic = convertInDictionaryAdmin(admin_list)
                        print("The list of admins are")
                        for i,details in admin_dic.items():
                            print(f"{i}->{details['email']} {details['password']}")
                        continue
                    elif admin_choice == "3":
                        print("See you again")
                        break
                    else:
                        print("Please select the choices from the menu..")
                        continue
                break
            else:
                print("You entered the wrong password")
                continue
        elif choice1.lower()=="no":
            print("You are out of admin menu")
            break
        else:
            print("Please enter either yes or no")
            continue
    while counter>0:
        print("Please enter your login credentials")
        login_mail = input("Please enter your mail id")
        login_password = input("Please enter your password")
        search_query = "SELECT * FROM admin WHERE email = ? AND password = ?"
        cursor.execute(search_query,(login_mail,login_password,))
        search_result = cursor.fetchone()
        if search_result:
            print("Welcome to the database...")
            login_state = True
            break
        else:
            counter-=1
            print("sorry wrong credentials..")
            print(f"You have only {counter} attempts left")
    if login_state:
        print("Here is the user db")
    else:
        print("The program is shuting down")                        
    connection.close()
except sqlite3.Error as e:
    print(e)    