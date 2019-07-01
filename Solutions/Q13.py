# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

in_str = input()
words = in_str.split()

letters = digits = 0
for word in words:
    for char in word:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
