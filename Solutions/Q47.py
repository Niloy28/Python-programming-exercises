# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

filtered_list = list(filter(lambda number: not number %
                            2, [x for x in range(1, 20 + 1)]))

print(filtered_list)
