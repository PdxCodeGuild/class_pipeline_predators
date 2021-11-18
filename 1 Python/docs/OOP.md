## Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data:

Classes are a way to structure data in a way that is easy to manage and easy to build upon. By data I mean attributes and methods. A method is a function related to a class. Attributes are values.

A class is a user-defined blueprint or prototype from which objects are created. Creating a new class creates a new type of object, allowing new instances of that type to be made. An Object is an instance of a Class. 


## Classes - instantiation

```python
class Employee:
      pass

empl_1 = Employee()
empl_2 = Employee()
```

The class Employee is the blueprint, and empl_1 & empl_2 are *instances* of that class. If you remember I mentioned that everything is an **object** in Python. A dictionary, an integer, a boolean are all instances of classes. When we make a list using `[]` syntax, we are instantiating a new instance of the **List** class. 

```Python
print(type([]))
#returns <class 'list'>
```

## Classes - attributes

Let's start building our model:

```python
class Employee:
 pass
 
empl_1 = Employee()
empl_2 = Employee()
 
empl_1.first = 'Alex'
empl_1.last = 'D'
empl_1.pay = 50
empl_1.email = 'alex.d@gmail.com'
 
 
empl_2.first = 'Bruce'
empl_2.last = 'Wayne'
empl_2.pay = 200
empl_2.email = 'batman@gmail.com'
 
print(empl_1.first, empl_2.first )
```

How inefficient is this method? A lot! If we had 50 employees, we would need to repeat the process several times. But there's a better way!


```python
class Employee:
    def __init__(self, first,last ,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
 
empl_1 = Employee('alex', 'd', 50)
empl_2 = Employee('Bruce', 'Wayne', 60)
 
print(empl_1.email, empl_2.email )
```

__init__ is a python "magic method"; it identifies a special kind of function called a constructor. Constructors are used to create class instances. So, when we define an __init__ method on a class, we can specify exactly how that class gets created. 

## Classes - Methods

Methods are functions within your class:

```python
class Employee:
    def __init__(self, first,last ,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
        def fullname(self):
            return self.first + ' ' + self.last
 
 
print(empl_1.fullname())
```