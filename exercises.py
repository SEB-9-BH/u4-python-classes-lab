import random

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)

    def deposit(self, amount):
        if amount <= 0:
            print("pro you dont have money :).")
            return self.balance
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            print("pro you dont have money :).")
            return self.balance
        if amount > self.balance:
            print("Insufficient funds.")
            return self.balance
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance



acc1 = BankAccount("Khalil", 500)
acc2 = BankAccount("Ali", 1000)

acc1.deposit(200)
acc1.withdraw(100)

acc2.deposit(500)
acc2.withdraw(2000)   

print("\n--- Account 1 ---")
print("Owner:", acc1.owner)
print("Account No: (khalil)", acc1.account_no)
print("Balance: (khalil)", acc1.balance)

print("\n--- Account 2 ---")
print("Owner:", acc2.owner)
print("Account No: (Ali)", acc2.account_no)
print("Balance: (Ali)", acc2.balance)
