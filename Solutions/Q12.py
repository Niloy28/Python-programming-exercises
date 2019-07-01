# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

even = []

for number in range(2000, 3001):
    i = number
    while i != 0:
        if (i % 10) % 2:
            break
        i //= 10
    if i == 0:
        even.append(str(number))

print(','.join(even))
