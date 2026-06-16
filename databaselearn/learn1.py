import sqlite3
import os
from datetime import datetime
working_dir = os.path.dirname(__file__)
new_db = os.path.join(working_dir,"database1")
try:
    os.makedirs(new_db,exist_ok=True)
    print("Database created")
except:
    print("There was some problem")
database_1 = os.path.join(new_db,"movies.db")
connection = sqlite3.connect(database_1)
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_Keys = ON;")
create_table = '''CREATE TABLE IF NOT EXISTS user(
                uid INTEGER PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INTEGER CHECK(age>0));'''
try:
    cursor.execute(create_table)
    connection.commit()
    print("User table created successfully")
except sqlite3.Error as e:
    print(e)
create_table_2 = '''CREATE TABLE IF NOT EXISTS movies(
                    mid INTEGER PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    mgenre VARCHAR(50),
                    mdate DATE);'''
try:
    cursor.execute(create_table_2)
    connection.commit()
    print("created the movie table")
except sqlite3.Error as e:
    print(e)
create_table_3 = ''' CREATE TABLE IF NOT EXISTS watch(
                    wid INTEGER PRIMARY KEY,
                    uid INTEGER NOT NULL,
                    mid INTEGER NOT NULL,
                    rate INTEGER CHECK(rate BETWEEN 0 AND 5),
                    wdate DATE,
                    wdevice VARCHAR(50),
                    FOREIGN KEY (uid) REFERENCES user(uid),
                    FOREIGN KEY (mid) REFERENCES movies(mid),
                    UNIQUE(uid,mid));'''
try:
    cursor.execute(create_table_3)
    connection.commit()
    print("Watch table created successfully")
except sqlite3.Error as e:
    print(e)
def EnterUser():
    while True:
        try:
            id = int(input("Enter the id"))
            break
        except ValueError:
            print("Please enter in numerics")
            continue
    name = input("Enter the name of the user")
    while True:
        try:
            age = int(input("Enter the age of the user. and please enter number above 0"))
            break
        except ValueError:
            print("Please enter in number")
            continue
    enter_querry = "INSERT INTO user (uid,name,age) values (?,?,?)"
    try:
        cursor.execute(enter_querry,(id,name,age))
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    return True
def movies():
    while True:
        try:
            mid = int(input("Enter the movie id"))
            break
        except ValueError:
            print("Enter value in number")
            continue
    name = input("Enter the name of the movie")
    mgenre = input("Input the genre of the movie")
    while True:
        mdate = input("Enter movie release date YYYY-MM-DD")
        try:
            datetime.strptime(mdate, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter in the correct format eg. 2001-11-02")
            continue
    insert_querry = "INSERT INTO movies(mid,name,mgenre,mdate) VALUES (?,?,?,?)"
    try:
        cursor.execute(insert_querry,(mid,name,mgenre,mdate))
        connection.commit()
        print("Value successfully added in the movies database")
    except sqlite3.Error as e:
        print(e)
    return True
def watchList():
    while True:
        try:
            wid = int(input("Enter the id in numeric"))
            break
        except ValueError as e:
            print(e)
            continue
    while True:
        try:
            uid = int(input("Enter the user id in numeric"))
            break
        except ValueError as e:
            print(e)
            continue
    while True:
        try:
            mid = int(input("Enter the movie id in numeric"))
            break
        except ValueError as e:
            print(e)
            continue
    while True:
        try:
            rating = int(input("Enter rating between 1 and 5"))
        except ValueError as e:
            print(e)
            continue
        if 1<=rating<=5:
            break
        else:
            print(f"{rating} should be between 1 and 5")
            continue
    while True:    
        wdate = input("Date in format YYYY-MM-DD")
        try:
            datetime.strptime(wdate,"%Y-%m-%d")
            break
        except ValueError as e:
            print(e)
            print("Please input in the format of YYYY-MM-DD")
            continue
    device = input("Please input the device type")
    insert_querry = "INSERT INTO watch (wid,uid,mid,rate,wdate,wdevice) VALUES (?,?,?,?,?,?)"
    try:
        cursor.execute(insert_querry,(wid,uid,mid,rating,wdate,device))
        connection.comit()
    except sqlite3.Error as e:
        print(e)
    return True
def printList(select):
    table_list = {"user": "user",
                  "movies": "movies",
                  "watch":"watch"}
    if select not in table_list:
        print(f"{select} list is not present")
        return False
    querry = f"SELECT * FROM {table_list[select]}"
    try:
        cursor.execute(querry)
        value = cursor.fetchall()
        for i in value:
            print(i)
    except sqlite3.Error as e:
        print(e)
    return True
def Exit():
    print("Exiting...")
    return False
choices = {"user": EnterUser,
           "movies": movies,
           "watch":watchList,
           "print": printList,
           "exit": Exit}
while True:
    choice = input(" | ".join(choices.keys()).upper()).lower()
    if choice in choices:
        if choice=="print":
            select = input("User/Movie/Watchlist").lower()
            view = choices[choice](select)
            if not view:
                print("Please select from the above mention list")
                continue
        elif not choices[choice]():
            print("Exiting")
            break
    else:
        print("Please choose from the above list of choices")
connection.close()