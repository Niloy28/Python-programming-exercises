# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension

import random

numbers = [x for x in range(0, 10 + 1) if x % 2 == 0]

print(random.choice(numbers))
