# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].


def square(number):
    return number ** 2


given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# using lambda
square_list = list(map(lambda square: square ** 2, given_list))

# using function
square_list = list(map(square, given_list))

print(square_list)
