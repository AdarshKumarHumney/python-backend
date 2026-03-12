import sqlite3
import os
def convertInDictionaryAdmin(list1):
    return {i[0]:{
        "email":i[1],
        "password":i[2]
    }for i in list1
    }
def convertInDictionaryUser(list2):
    return {i[0]:{
        "name":i[1],
        "email":i[2],
        "age":i[3]
    }for i in list2}
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
    cursor.execute(create_user)
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
        while True:
            print("Welcome to the user database")
            print("-----Menu-----")
            userchoice = input("1. Add user\n""2.Search user\n""3.Update User\n""4.Delete User\n""5.Print\n""6.Exit\n" )
            if userchoice=="1":
                user_name = input("User name")
                user_email = input("User email")
                search_user_query = "SELECT * FROM user WHERE email = ?"
                cursor.execute(search_user_query,(user_email,))
                find = cursor.fetchone()
                if find:
                    print("email is already being used. Try different emails")
                    continue
                else:
                    try:
                        user_age = int(input("User age"))
                    except ValueError:
                        print("please put ages in digits and not alplhabets")    
                        continue
                    insert_query= "INSERT INTO user (name, email, age) VALUES (?,?,?)"
                    cursor.execute(insert_query,(user_name,user_email,user_age,))
                    connection.commit()
                    print(f"{user_name} added to the database successfully")
                continue
            elif userchoice == "2":
                search_choice = input("1.Search by Id\n""2.Search by name\n""3.Search by email\n")
                if search_choice=="1":
                    while True:
                        try:
                            search_id=int(input("Please input the id that you want to search"))
                            break
                        except ValueError:
                            print("Please input id in numerical value")
                            continue    
                    search_Id_querry = "SELECT * FROM user WHERE id =?"
                    cursor.execute(search_Id_querry,(search_id,))
                    find_id = cursor.fetchone()
                    if find_id:
                        print(find_id)
                        continue
                    else:
                        print("Id was not found")
                        continue
                elif search_choice == "2":
                    search_name = input("Please enter the name that you want to search")
                    search_name_querry = "SELECT * FROM user WHERE name = ?"
                    cursor.execute(search_name_querry,(search_name,))
                    find_name = cursor.fetchall() 
                    if find_name:
                        list2 = convertInDictionaryUser(find_name)
                        for i,details in list2.items():
                            print(f"{i}->{details}")
                        continue
                    else:
                        print(f"the database does not have any user with {search_name}")
                        continue
                elif search_choice== "3":
                    search_mail=input("Please input the mail that you want to search")
                    search_mail_querry = "SELECT * FROM user WHERE email =?"
                    cursor.execute(search_mail_querry,(search_mail,))
                    find_mail = cursor.fetchone()
                    if find_mail:
                        print(find_mail)
                        continue
                    else:
                        print("mail was not found")
                        continue
                else:
                    print("You have entered a wrong input")
                    continue
            elif userchoice == "3":
                print("Here is a list of our users")
                user_search_querry = "SELECT * FROM user"
                cursor.execute(user_search_querry)
                user_list = cursor.fetchall()
                if user_list:
                    list3 = convertInDictionaryUser(user_list)
                    for i,details in list3.items():
                        print(f"{i}->{details}")
                    while True:
                        try:    
                            update_choice_id = int(input("Please select the id of the user from above list that you want to update"))
                            break
                        except ValueError:
                            print("Please use a numerical value for the id")
                            continue
                    search_user_id = "SELECT * FROM user WHERE id = ?"
                    cursor.execute(search_user_id,(update_choice_id,))
                    found_id1 = cursor.fetchone()
                    if found_id1:
                        update_choice_menu= input("What do you want to update? Name or email or age of the user")
                        if update_choice_menu.lower()=="name":
                            update_name = input("Please enter the new name")
                            update_querry = "UPDATE user SET name =? WHERE id =? "
                            cursor.execute(update_querry,(update_name,update_choice_id,))
                            connection.commit()
                            print("Username changed successfully")
                            continue
                        elif update_choice_menu.lower()=="email":
                            update_email = input("Please input a newmail")
                            search_mail_update = "SELECT * FROM user WHERE email = ?"
                            cursor.execute(search_mail_update,(update_email,))
                            found_mail = cursor.fetchone()
                            if found_mail:
                                print("the mail you entered is already in the list please enter a new mail")
                                continue
                            else:
                                update_mail_querry = "UPDATE user SET email = ? WHERE id = ?"
                                cursor.execute(update_mail_querry,(update_email,update_choice_id))
                                connection.commit()
                                print("mail was updated successfully")
                                continue
                        elif update_choice_menu.lower()=="age":
                            while True:
                                try:
                                    update_age = int(input("Please enter new age"))
                                    break
                                except ValueError:
                                    print("Please input age in digits")
                                    continue    
                            update_age_querry = "UPDATE user SET age =? WHERE id =?"
                            cursor.execute(update_age_querry,(update_age,update_choice_id))
                            connection.commit()
                            print("Age was updated of the user")
                            continue
                        else:
                            print("Wrong input")
                            continue
                    else:
                        print("The id that you are looking for is not in the database")
                        continue
            elif userchoice=="4":
                print("Here is the list of user")
                user_list_2 = "SELECT * FROM user"
                cursor.execute(user_list_2)
                list4 = cursor.fetchall()
                delete_list = convertInDictionaryUser(list4)
                for i,details in delete_list.items():
                    print(f"{i}->{details}")
                while True:
                    try:
                        delete_id = int(input("Select the id that you want to delete from the database"))
                        break
                    except ValueError:
                        print("Please use a numerical value for the id")
                        continue
                search_delete_id= "SELECT * FROM user WHERE id =?"
                cursor.execute(search_delete_id,(delete_id,))
                found_id = cursor.fetchone()
                if found_id:
                    print(found_id)
                    confirmation = input("Are you sure that you want to delete the user above")
                    if confirmation.lower()=="yes":
                        delete_id_querry = "DELETE FROM user WHERE id = ?"
                        cursor.execute(delete_id_querry,(delete_id,))
                        connection.commit()
                        print("User deleted successfully")
                        continue
                    elif confirmation.lower()=="no":
                        print("going back to main menu")
                        continue
                    else:
                        print("You have entered the wrong input")
                        continue
                else:
                    print("The id the you are looking for is not in the database")
                    continue
            elif userchoice =="5":
                print("Here are the list of the user in your database")
                list_user_querry = "SELECT * FROM user"
                cursor.execute(list_user_querry)
                list_user = cursor.fetchall()
                convert_list = convertInDictionaryUser(list_user)
                for i,details in convert_list.items():
                    print(f"{i}->{details}")
                continue            
            elif userchoice=="6":
                print("admin loginoff.")
                break
            else:
                print("Please select options from the above menu")
                continue        
    else:
        print("The program is shuting down")                     
    connection.close()
except sqlite3.Error as e:
    print(e)    