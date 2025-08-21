class BankAccount:
    def __init__(self, name, balance=0.0):  # Fixed typo: should be __init__, not _init_
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance
# Example usage:
# Create a new bank account for Alice with an initial balance of 1000
name = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(name, initial_balance)
# Deposit 500 into Alice's account
account.deposit(500)
# Withdraw 200 from Alice's account
account.withdraw(200)
# Check the current balance
account.check_balance()
# --- Explanation ---
# The BankAccount class models a simple bank account with basic operations.
# - The _init_ method initializes the account holder's name and starting balance.
# - The deposit method adds a positive amount to the balance.
# - The withdraw method subtracts a positive amount from the balance if sufficient funds are available.
# - The check_balance method prints and returns the current balance.
# Example usage demonstrates creating an account, depositing, withdrawing, and checking the balance.