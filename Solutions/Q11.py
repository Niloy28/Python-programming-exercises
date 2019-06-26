string = input()

bin_list = string.split(',')

print_list = []
for num in bin_list:
    if int(num, 2) % 5 == 0:
        print_list.append(num)

print(','.join(print_list))
