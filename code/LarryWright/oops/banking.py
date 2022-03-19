import requests
class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountnumber = 1234
        self.name = "Larry Wright"
        self.balance = 500

    def get_balance(self):
        return self.balance    
    def deposit(self, amount):
        self.balance += amount
        print(f' Current balance is {self.balance}')
    def withdraw(self, amount):
        if amount > self.balance:
            print('insufficient funds')
        else:
            self.balance -= amount
    def bank_fees(self, amount):
        amount * .05
    def display(self):
        print(f'Hello{self.name},''Accout number:'' {self.accountnumber},''You balance is:''{self.balance}')