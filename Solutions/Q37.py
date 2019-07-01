# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.


def printList(start, end, no_of_elements=5):
    l = [i ** 2 for i in range(start, end + 1)]

    print(l[:no_of_elements])


printList(1, 20)
