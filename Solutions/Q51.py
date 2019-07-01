# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.


class Circle(object):
    PI = 3.1416

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2


circle = Circle(5.0)
print(f"{circle.area():.2f}")
