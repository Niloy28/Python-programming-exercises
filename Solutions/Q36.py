# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).


def printList(start, end):
    l = [i ** 2 for i in range(start, end + 1)]

    print(l)


printList(1, 20)
