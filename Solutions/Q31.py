# Define a function that can accept an integer number as input and print the "It is an even number"
# if the number is even, otherwise print "It is an odd number".

def determineEvenOrOdd(x):
    '''Prints whether x is even or odd'''
    if x % 2:
        print("It is an odd number.")
    else:
        print("It is an even number.")


determineEvenOrOdd(4)
