# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

import random


def generator(start=100, end=200):
    for i in range(start, end+1):
        if i % 2 == 0:
            yield i


print(random.sample(list(generator()), k=5))
