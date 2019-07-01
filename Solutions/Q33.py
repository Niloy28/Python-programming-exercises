# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

from collections import defaultdict


def printDictionary(start, end):
    dictionary = dict()

    for i in range(start, end + 1):
        dictionary[i] = i ** 2

    print(dictionary)


printDictionary(1, 20)
