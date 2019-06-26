cash = 0

while True:
    s = input()

    if not s:
        break

    values = s.split()
    if values[0].lower() == 'd':
        cash += int(values[1])
    elif values[0].lower() == 'w':
        cash -= int(values[1])

print(cash)
