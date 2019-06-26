import math

C = 50
H = 30
vals = input()
d = vals.split(',')

q = []
for i in d:
    q.append(str(round(math.sqrt((2 * C * int(i)) / H))))

print(','.join(q))
