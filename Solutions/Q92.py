# Please write a program which count and print the numbers of each character in a string input by console.

# Example:
# If the following string is given as input to the program:
# abcdefgabc

# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

from collections import defaultdict

string = input()

occurrences = dict()

for character in string:
    occurrences[character] = occurrences.get(character, 0) + 1

for (key, val) in occurrences.items():
    print(f"{key},{val}")
