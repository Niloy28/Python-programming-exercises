input_str = input()
dimensions = [int(x) for x in input_str.split(',')]

row = dimensions[0]
col = dimensions[1]

# conventional method
array = [[0 for i in range(0, col)] for j in range(0, row)]
for i in range(0, row):
    for j in range(0, col):
        array[i][j] = i * j

# using list comprehension
multilist = [i * j for i in range(0, col)] for j in range(0, row)]

print(array)
print(multilist)
