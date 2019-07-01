# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

def printLongerString(s1, s2):
    '''Prints the longer one of s1 and s2
    If their lengths are equal, both are printed'''
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)


s1 = input()
s2 = input()

printLongerString(s1, s2)
