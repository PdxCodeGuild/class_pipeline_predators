class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
    def display(self):
        print(f'Account name: {self.name}')
        print(f'Account number: {self.number}')
        print(f'Account balance: {self.balance}')
info = Account('Tianyang', 123456789, 50)
info.display()
class Amount: 
    def __init__(self):
        self.__balance = 50
    def deposit(self, amount):
        self.__balance += amount
        print(f'Current balance: {self.__balance}')
    def withdraw(self, amount):
        if amount > self.__balance:
            print("You don't have enough money")
        else: 
            self.__balance -= amount
            print(f'Current balance: {self.__balance}')
    def bank_fee(self):
        self.__balance = 0.05*self.__balance
        print(f'Bank fee: {self.__balance}')
tianyang_account = Amount()
tianyang_account.deposit(1000)
tianyang_account.withdraw(2000)
tianyang_account.withdraw(500)
tianyang_account.bank_fee()

