import random

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return self.balance
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"Account {self.account_no} - Balance: {self.balance:.2f}"

alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob")

print(alice)
alice.deposit(250)
print(alice)

print(bob)
bob.deposit(500)
print(bob)
bob.withdraw(500)
print(bob)
