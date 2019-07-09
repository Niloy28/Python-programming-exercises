# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

import random


def generator(start=100, end=200):
    for i in range(start, end+1):
        yield i


print(random.sample(list(generator()), k=5))
