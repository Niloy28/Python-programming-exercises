input_str = input()
dimensions = [int(x) for x in input_str.split(',')]

x = dimensions[0]
y = dimensions[1]

array = [[0 for i in range(0, y)] for j in range(0, x)]
for i in range(0, x):
    for j in range(0, y):
        array[i][j] = i * j

print(array)
