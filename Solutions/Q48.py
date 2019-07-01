# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

square_list = list(
    map(lambda num: num ** 2, [number for number in range(1, 20 + 1)]))

print(square_list)
