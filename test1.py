print("-----quick calculator-------")
user_input = input("Enter a number to multiply by 10- ")
try:
    number = int(user_input)
    result = number*10
    print(f"Your result is {result}")
except ValueError:
    print("Please enter in the digits")    
print("program completed successfully")
