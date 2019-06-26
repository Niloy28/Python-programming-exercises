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
