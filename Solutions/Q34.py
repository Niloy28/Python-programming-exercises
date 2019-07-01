# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# The function should just print the values only.

from collections import defaultdict


def printDictionaryValues(start, end):
    dictionary = dict()

    for i in range(start, end + 1):
        dictionary[i] = i ** 2

    dict_keys = dictionary.keys()
    for key in dict_keys:
        print(dictionary[key])


printDictionaryValues(1, 20)
