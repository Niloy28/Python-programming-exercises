# Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

import random


def generator(start=1, end=1000):
    for i in range(start, end+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i


print(random.sample(list(generator()), k=5))
