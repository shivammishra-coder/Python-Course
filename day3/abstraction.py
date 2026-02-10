from abc import ABC, abstractmethod
import math

# The Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Create instances of the subclasses
my_circle = Circle(5)
my_rectangle = Rectangle(10, 5)

# Treat them as a list of "Shapes"
shapes_list = [my_circle, my_rectangle]

for shape in shapes_list:
    
    print(f"Area: {shape.calculate_area():.2f}")