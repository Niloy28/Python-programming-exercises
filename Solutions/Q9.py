sequence = []

while True:
    s = input()
    if s:
        sequence.append(s.upper())
    else:
        break

for i in sequence:
    print(i)
