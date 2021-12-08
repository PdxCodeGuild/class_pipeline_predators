class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def find_area(self):
        return self.length * self.width

    def find_perim(self):
        return 2 * (self.length + self.width)
    
    def display(self):
        print(f'\nLength: {self.length} Width: {self.width} Area: {self.find_area()} Permimeter: {self.find_perim()}')

my_rectangle = Rectangle(2,4)
my_rectangle.display()

class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def find_volume(self):
        return self.length * self.width * self.height

my_parallelepiped = Parallelepiped(2, 4, 6)
print(f'\nParallelepiped Volume: {my_parallelepiped.find_volume()}')