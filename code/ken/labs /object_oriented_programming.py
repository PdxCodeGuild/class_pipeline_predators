# Lab: Object Oriented Programming


### Bank Account Class

# - Create a Python class called BankAccount which represents a bank account
# having as attributes: account_number (integer), name (name of the account owner as string type), balance.
# - Create a constructor with parameters: account_number, name, balance. 
class BankAccount:
    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance

# - Create a deposit() method which manages the deposit actions.
#deposit adds to the account ammount
#you will need balance from the constructor
#deposit = self balance plus deposit

    def deposit(self, deposit_ammount ):
        self.balance += deposit_ammount
        print(self.balance)
        return self.balance  

# - Create a withdrawal() method  which manages withdrawals actions.
    def withdrawal(self, withdrawal_ammount):
        self.balance -= withdrawal_ammount
        print(self.balance)
        return self.balance

# - Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
    def bankFees(self):
        self.balance *= 1.05
        print(self.balance)
        return self.balance

# - Create a display() method to display account details.
    def display(self):
        print(f"Hi {self.name} your balance for account number #{self.number} is {self.balance}")

#How I would use an instance of the bank         
account = BankAccount(13974268 , 'jim jones', 900 )
account.deposit(20)
account.withdrawal(100)
account.bankFees()
account.display()



"""
### Rectangle Class

- Write a Rectangle class in Python language, allowing you to build a rectangle with **length** and **width** attributes.
- Create a perimeter() method to calculate the perimeter of the rectangle and a area() method to calculate the area of ​​the rectangle.
- Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
- Create a Parallelepiped child class inheriting from the Rectangle class and with a **height** attribute and another volume() method to calculate the volume of the Parallelepiped.

### Person Class

- Create a class Person with attributes: **name** and **age** of type string.
- Create a display() method that displays the name and age of an object created via the Person class.
- Create a child class Student which inherits from the Person class and which also has a **favourite_hobby** attribute.
- Create a method displayStudent() that displays the name, age and favourite_hobby of an object created via the Student class.
"""