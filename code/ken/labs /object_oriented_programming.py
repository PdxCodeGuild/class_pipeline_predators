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




### Rectangle Class

# - Write a Rectangle class in Python language, allowing you to build a rectangle with **length** and **width** attributes.
class Rectangle:
    def __init__(self, rectangle_length, rectangle_width):
        self.rectangle_length = rectangle_length
        self.rectangle_width = rectangle_width
        self.__rectangle_perimeter = 0
        self.__rectangle_area = 0 
        
# - Create a perimeter() method to calculate the perimeter of the rectangle 
    def perimeter(self):
        self.__rectangle_perimeter = self.__rectangle_perimeter + (self.rectangle_width * 2) + (self.rectangle_length * 2)
        print(self.__rectangle_perimeter)
        return self.__rectangle_perimeter
# and a area() method to calculate the area of ​​the rectangle.
    def area(self):
        self.__rectangle_area = self.rectangle_length * self.rectangle_width
        print(self.__rectangle_area)
        return self.__rectangle_area
# - Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
    def display(self):
        print(f" This rectangles length is {self.rectangle_length} the width is {self.rectangle_width} the perimeter is {self.__rectangle_perimeter} and the area is {self.__rectangle_area}"
        )
# - Create a Parallelepiped child class inheriting from the Rectangle class and with a **height** attribute and another volume() method to calculate the volume of the Parallelepiped.
class Parallelepiped(Rectangle):
    def __init__(self, rectangle_length, rectangle_width, para_height):
        super().__init__(rectangle_length, rectangle_width)
        self.para_height = para_height

    def volume(self):
        volume_para = self.para_height * self.rectangle_length * self.rectangle_width
        print(volume_para)

this_rectangle = Rectangle(5,8)
this_rectangle.perimeter()
this_rectangle.area()
this_rectangle.display()

this_para = Parallelepiped(9,1,2)
this_para.volume()



### Person Class

# - Create a class Person with attributes: **name** and **age** of type string.
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name 

# - Create a display() method that displays the name and age of an object created via the Person class.
    def display(self):
        print(f"{self.name}'s age is {self.age}")
# - Create a child class Student which inherits from the Person class and which also has a **favourite_hobby** attribute.
class Student(Person):
    def __init__(self, name, age, fav_hob):
        super().__init__(name, age)
        self.fav_hob = fav_hob

# - Create a method displayStudent() that displays the name, age and favourite_hobby of an object created via the Student class.
    def display(self):
        print(f"{self.name} is {self.age} years old and loves to {self.fav_hob}")

me_per = Person("Frank Wimbledon", "33")
me_per.display()

new_per = Student("Frankie Wilterton", "95", "disc golf")
new_per.display()

