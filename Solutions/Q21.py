# A robot moves in a plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

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
