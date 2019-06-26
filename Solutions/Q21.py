from math import pow, sqrt

origin = (0, 0)

destination = [0, 0]
while True:
    s = input()
    if not s:
        break

    instruction = s.split()
    if instruction[0].upper() == "UP":
        destination[1] += int(instruction[1])
    if instruction[0].upper() == "DOWN":
        destination[1] -= int(instruction[1])
    if instruction[0].upper() == "LEFT":
        destination[0] -= int(instruction[1])
    if instruction[0].upper() == "RIGHT":
        destination[0] += int(instruction[1])

distance = round(sqrt(
    pow(destination[0] - origin[0], 2) + pow(destination[1] - origin[1], 2)))

print(distance)
