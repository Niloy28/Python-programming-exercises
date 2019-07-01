# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.


class Shape(object):
    def __init__(self, length=0):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


shape = Shape()
square = Square(3)

print(f"{shape.area():.2f}")
print(f"{square.area():.2f}")
