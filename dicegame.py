import random
import time
balance = 100
while True:
    answer = input("Do you wish to bet please answer yes or quit")
    if answer.lower()=="yes":    
        print(f"you have Rs.{balance} how much you wanna bet")
        try:
            choice = int(input())
        except ValueError:
            print("please enter a valid number")
            continue
        if choice <=0:
            print("be serious and restart")
            continue
        if choice >balance:
            print("insufficient funds")
            continue
        else:
            print("rolling dice")
            time.sleep(2)
            result = random.randint(1,6)+random.randint(1,6)
            print(f"{result}")
            if result>7:
                print("you win")
                balance+=choice
            else:
                balance = balance-choice
        print(f"your new balance is {balance}")
        if balance ==0:
            print("you are broke")
            break
    elif answer.lower()=="quit":
        print(f"you are leaving with Rs.{balance}, come again")
        break
    else:
        print("please provide with yes/quit")
