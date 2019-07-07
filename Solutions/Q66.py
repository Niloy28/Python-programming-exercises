# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.


def even_generator(n):
    for i in range(n + 1):
        if not i % 2:
            yield i


n = int(input())
l = list(even_generator(n))
l = [str(i) for i in l]

print(','.join(l))
