# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].


def is_even(number):
    return not number % 2


given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# using lambda
filtered_list = filter(lambda x: not x % 2, given_list)

# using function
filtered_list = filter(is_even, given_list)

filtered_list = list(filtered_list)

print(filtered_list)
