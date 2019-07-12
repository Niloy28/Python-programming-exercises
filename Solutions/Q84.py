# By using list comprehension, please write a program to print the list after removing the numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

numbers = [12, 24, 35, 70, 88, 120, 155]

trimmed_list = [x for x in numbers if x % 5 == 0 and x % 7 == 0]

print(trimmed_list)
