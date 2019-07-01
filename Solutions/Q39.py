# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list.


def printListExceptSpecified(start, end, start_of_skip=0, no_of_elem_to_skip=5):
    l = [i ** 2 for i in range(start, end + 1)]

    l = l[start_of_skip + no_of_elem_to_skip:]
    print(l)


printListExceptSpecified(1, 20)
