from types import ClassMethodDescriptorType

class BankAccount:
    def __init__(self, first, last, act_num, bal):
        self.first = first
        self.last = last
        self.name = last + ', ' + first
        self.act_num = act_num
        self.balance = bal
    
    def deposit(self, amount):
        self.balance += amount

    def bank_fees(self):
        return int(self.balance * .05)

    def withdraw(self, amount):
        if amount > self.balance:
            print('not enough funds')
        else:
            self.balance -= amount

    def display(self):
        print(f'\n{self.name} Acct# {self.act_num} Balance: ${self.balance} Fees: ${self.bank_fees()}')

scott_account= BankAccount('Scott', 'Moore', 1234567, 1000)

scott_account.deposit(1000)
scott_account.withdraw(500)

scott_account.display()