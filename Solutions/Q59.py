# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

import re

words = input()

digit_words = re.findall(r"\d+", words)
if digit_words:
    print(digit_words)
