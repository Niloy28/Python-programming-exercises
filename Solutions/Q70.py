# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


def binary_search(sorted_list, item):
    start = 0
    end = len(sorted_list) - 1

    middle = (start + end) // 2
    while(sorted_list[middle] != item):
        if item < sorted_list[middle]:
            end = middle - 1
        elif item > sorted_list[middle]:
            start = middle + 1
        else:
            break

        middle = (start + end) // 2

    if start > end:
        return None

    return middle


l = [2, 3, 1, 6, 8, 9, 0, 7, 4, 10, 5]

print(binary_search(sorted(l), 4))
