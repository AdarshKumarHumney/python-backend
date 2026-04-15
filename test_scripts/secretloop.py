import random
secret_number = random.randint(1,100)
attempt = 0
while True:
    try:
        user_inp = int(input("Take a guess from 1 to 100"))
    except ValueError:
        print("that is not an integer please input an integer")
        continue
    attempt+=1
    if user_inp==secret_number:
        print(f"you guessed it correctly in {attempt} attempts")
        break
    elif user_inp>secret_number:
        print("guess too high,  please try again")
    else:
        print("guess too low, please try again")    