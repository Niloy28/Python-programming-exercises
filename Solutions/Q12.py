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
