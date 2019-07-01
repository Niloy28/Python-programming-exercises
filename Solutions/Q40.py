# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).


def printTuple(start, end):
    t = tuple([i ** 2 for i in range(start, end + 1)])

    print(t)


printTuple(1, 20)
