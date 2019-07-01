# Define a class, which have a class parameter and have a same instance parameter.

class Person(object):
    def __init__(self, name=None):
        self.name = name


jeff = Person("Jeff")

print(jeff.name)
