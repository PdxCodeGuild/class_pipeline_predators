class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f'Name: {self.name} \nAge: {self.age}')
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def display(self):
        return super().display()
info_1 = Person('Tianyang', 30)
info_1.display()
info_2 = Student('Joe', 31)
info_2.display()    