# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# The function should just print the keys only.

from collections import defaultdict


def printDictionaryKeys(start, end):
    dictionary = dict()

    for i in range(start, end + 1):
        dictionary[i] = i ** 2

    for key in dictionary.keys():
        print(key)


printDictionaryKeys(1, 20)
