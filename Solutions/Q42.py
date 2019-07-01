# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).


given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_tuple = tuple([x for x in given_tuple if not x % 2])

print(even_tuple)
