# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.


class Rectangle(object):
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rect = Rectangle(5, 2)
print(f"{rect.area():.3f}")
