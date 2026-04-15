class BankAccount:
    def __init__(self,owner_name,balance):
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{self.owner_name} deposited {amount} new balance is {self.balance}")
    def show_balance(self):
        print(f"{self.owner_name} balnce:{self.balance}")
acct1 = BankAccount("Adasrh",500)        
acct2 = BankAccount("Gemini",0)
acct1.show_balance()
acct1.deposit(500)
acct1.deposit(600)
acct2.show_balance()
acct1.show_balance()