# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

first_half = t[:len(t) // 2]
last_half = t[len(first_half):]

print(first_half)
print(last_half)
