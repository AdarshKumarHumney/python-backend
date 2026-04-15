def withdraw_money(user_data,entered_pin,amount):
    if entered_pin==user_data['pin']:
        print("welcome")
        if amount<=user_data['balance']:
            print(f"withdrawl amount is {amount}")
            remaining=user_data['balance']-amount
            print(f"balance amount is {remaining} ")
        else:
            print("insufficient funds")
    else:
        print("wrong pin")            
user = {
    'name': 'Adarsh',
    'pin': 1234,
    'balance': 5000
}
print("Hello please enter the pin and the amount you want to withdrawl")
pass1 = int(input())
cash = int(input())
withdraw_money(user,pass1,cash)