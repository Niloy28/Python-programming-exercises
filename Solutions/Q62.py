# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

n = int(input())

sum = 0
try:
    for i in range(1, n + 1):
        sum += i / (i + 1)

    print(f"{sum:.3f}")
except ZeroDivisionError as error:
    print("n must be > 0!")
