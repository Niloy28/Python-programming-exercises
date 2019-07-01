# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

given_list = list(filter(lambda number: not number % 2, given_list))
given_list = list(map(lambda number: number ** 2, given_list))

print(given_list)
