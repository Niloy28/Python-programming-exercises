# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

def add(x, y):
    '''Returns the sum of 2 integers passed as strings'''
    return int(x) + int(y)


x = input()
y = input()

print(add(x, y))
