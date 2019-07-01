# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

in_str = input()
words = in_str.split()

upper_letters = lower_letters = 0
for word in words:
    for char in word:
        if char.isupper():
            upper_letters += 1
        elif char.islower():
            lower_letters += 1


print(f"UPPER CASE {upper_letters}")
print(f"LOWER CASE {lower_letters}")
