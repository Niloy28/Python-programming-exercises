# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

numbers = [12, 24, 35, 24, 88, 120, 155]

try:
    numbers.remove(24)

    print(numbers)
except ValueError as exception:
    print(exception)
