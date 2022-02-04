'''
Person Class
Create a Python class Person with attributes: name and age of type string.
Create a display() method that displays the name and age of an object created via the Person class.
Create a child class Student which inherits from the Person class and which also has a section attribute.
Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def name_age(self):
        print(f"Name: {self.name} age: {self.age}")
class Student(Person):
    def _init_(self,name,age,student):
        super()._init_(name,age)
        self.student = student
    def stu_mem(self):
        print(f"Name: {self.name} age: {self.age} is a student at PDX Code Guild") 


o = Person("Orian",41)
j = Student('Jane', 35)

j.stu_mem()
j.name_age()
o.name_age()



