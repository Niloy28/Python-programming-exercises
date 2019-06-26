from collections import defaultdict

frequency = dict()

s = input()
words = s.split()

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

keys = frequency.keys()
keys = sorted(keys)
for key in keys:
    print(f"{key}:{frequency[key]}")
