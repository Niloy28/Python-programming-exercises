from collections import defaultdict


def printDictionary():
    dictionary = dict()
    for i in range(1, 3 + 1):
        dictionary[i] = i ** 2

    print(dictionary)


printDictionary()
