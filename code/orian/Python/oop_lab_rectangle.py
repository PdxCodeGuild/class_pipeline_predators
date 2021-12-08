'''Rectangle Class
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.'''


class Rectangle:
    MEASURE_UNIT:('inches','feet','milimeters','meters')

    def __init__(self,length, width,units):
        self.length=length
        self.width=width
        self.MEASURE_UNIT=units 
    def perimeter(self):
        perimeter_rec = 2* (self.length + self.width) 
        print(f'The perimeter is {perimeter_rec} {self.MEASURE_UNIT}')
    def area(self):
        area_rec= self.length * self.width
        print(f'The area is {area_rec} square {self.MEASURE_UNIT}')
    

class Parallelepipede(Rectangle):
    def __init__(self,lenght,width,height,units):
        super().__init__(lenght,width,units)
        self.height=height
    def volume(self):
        volume_rec=(self.length * self.height * self.width)
        print(F'The volume is {volume_rec} cubic {self.MEASURE_UNIT}')


# user_class=input('What type of rectangle are you measuring? Enter 1 for 2D rectangle or enter 2 for rectangular cuboid:  ')
# user_height=input('Enter height of the rectangular cuboid: ')
# user_lenght=input('Enter lenght of the rectangle: ')
# user_width=input('Enter the width of the rectangle: ')
# user_unit=input("Enter the unit of measurement i.e. inches, feet, milimeters or meters: ")




user_class=input('What type of rectangle are you measuring? Enter 1 for (2D) rectangle or enter 2 for rectangular cuboid (3d):  ')


for user in user_class:
    if user_class == '1':
        user_lenght=int(input('Enter lenght of the rectangle: '))
        user_width=int(input('Enter the width of the rectangle: '))
        user_unit=input("Enter the unit of measurement i.e. inches, feet, milimeters or meters: ")
        user=Rectangle(user_lenght,user_width,user_unit)
        user.perimeter()
        user.area()
    if user_class == '2':
        user_lenght=int(input('Enter lenght of the rectangular cuboid: '))
        user_width=int(input('Enter the width of the rectangular cuboid: '))
        user_height=int(input('Enter height of the rectangular cuboid: '))
        user_unit=input("Enter the unit of measurement i.e. inches, feet, milimeters or meters: ")
        user=Parallelepipede(user_lenght,user_width,user_height,user_unit)
        user.perimeter()
        user.volume()
        user.area()
    
