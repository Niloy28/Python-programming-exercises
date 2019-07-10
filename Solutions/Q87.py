# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

numbers = [12,24,35,70,88,120,155]

l = [x for (i, x) in enumerate(numbers) if i != 0 and i != 4 and i != 5]

print(l)