# Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=1
# with a given n input by console (n>0).


def compute(number):
    if number == 0:
        return 1

    return compute(number - 1) + 100


n = int(input())

result = compute(n)

print(result)
