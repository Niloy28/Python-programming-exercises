# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

numbers = [5, 6, 77, 45, 22, 12, 24]

odds = [x for x in numbers if x % 2 != 0]

print(odds)
