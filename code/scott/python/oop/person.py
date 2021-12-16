class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f'\n{self.name}, Age: {self.age}')

class Student(Person):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby

    def display_student(self):
        print(f'\n{self.name}, Age: {self.age}, Hobby: {self.hobby}')

person = Person('S. Henry Moore', '56')
person.display()
student = Student('Amelia Michelle', '28', 'Ceramics')
student.display_student()
print()