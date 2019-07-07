# Define a custom exception class which takes a string message as attribute.


class CustomException(Exception):
    def __init__(self, message):
        self.error = message


error = CustomException("Mayday!")
