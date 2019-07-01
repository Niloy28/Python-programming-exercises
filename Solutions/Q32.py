# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included)
# and the values are square of keys.

from collections import defaultdict


def printDictionary():
    dictionary = dict()
    for i in range(1, 3 + 1):
        dictionary[i] = i ** 2

    print(dictionary)


printDictionary()
