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
