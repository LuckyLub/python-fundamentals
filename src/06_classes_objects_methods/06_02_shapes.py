'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''




class Circle:

    def __init__(self, radius):
        from math import pi
        self.radius = radius
        self.pi = pi

    def Area(self):
        return self.pi * self.radius ** 2

    def Perimeter(self):
        return self.pi * self.radius * 2

class Square:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def Area(self):
        return self.width * self.height

    def Perimeter(self):
        return self.width * 2 + self.height * 2

rond = Circle(5)
print(rond.Area(), rond.Perimeter())


vierkant = Square(5, 10)
print (vierkant.Area(), vierkant.Perimeter())