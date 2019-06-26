l = []

while True:
    s = input()
    if not s:
        break

    l.append(tuple(s.split(',')))

l = sorted(l, key=lambda element: (element[0:]))
print(l)
