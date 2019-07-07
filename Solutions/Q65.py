# The Fibonacci Sequence is computed based on the following formula:
# f(n) = 0 if n = 0
# f(n) = 1 if n = 1
# f(n) = f(n-1)+f(n-2) if n > 1

# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

from collections import defaultdict

memo = dict()


def fact(n):
    if n in memo.keys():
        return memo[n]

    f = 0
    if n == 0:
        f = 0
    elif n == 1:
        f = 1
    else:
        f = fact(n - 1) + fact(n - 2)

    memo[n] = f
    return f


n = int(input())

fact(n)
fib_seq = [str(val) for key, val in sorted(memo.items())]

print(','.join(fib_seq))
