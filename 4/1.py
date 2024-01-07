import math

class Triangle:
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.name = "Trójkąt"
        self.side = side

    def calculate_area(self):
        return math.sqrt(3)/4 * self.side ** 2
    
    def calculate_perimeter(self):
        return 3 * self.side

    def display_name(self):
        return self.name


class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.name = "Kwadrat"
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_name(self):
        return self.name


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.name = "Koło"
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def display_name(self):
        return self.name



triangle = Triangle(3)
print(triangle.display_name())
print(triangle.calculate_area())  
print(triangle.calculate_perimeter()) 

rectangle = Rectangle(12, 1)
print(rectangle.display_name())
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

circle = Circle(7)
print(circle.display_name())
print(circle.calculate_area())
print(circle.calculate_perimeter())
