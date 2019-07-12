# Please write a program to print the running time of execution of "1+1" for 100 times.

import timeit

count = 0
start_time = timeit.default_timer()
while count < 100:
    1 + 2
    count += 1
end_time = timeit.default_timer()

print(end_time - start_time)
