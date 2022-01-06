class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2*self.length+2*self.width
    def area(self):
        return self.length*self.width
    def display(self):
        print(f'The length is {self.length}')
        print(f'The width is {self.width}')
        print(f'The perimeter is {self.perimeter()}')
        print(f'The area is {self.area()}')
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        print(f'The volume is {self.area()*self.height}')
elesments = Rectangle(5,8)
elesments.display()
elesments = Parallelepipede(5,8,10)
elesments.volume()

