values = input()

odds = [number for number in values.split(',') if not int(number) % 2]

print(','.join(odds))
