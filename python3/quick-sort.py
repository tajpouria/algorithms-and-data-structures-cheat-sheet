#!/usr/bin/python3

def quick_sort(arr):
    if len(arr) <= 1: 
        return arr

    pivot = arr.pop()

    less_arr = []
    greater_arr = []

    for i in arr:
        if i <= pivot:
            less_arr.append(i)
        else:
            greater_arr.append(i)

    return quick_sort(less_arr) + [pivot] + quick_sort(greater_arr)


sorted_arr = quick_sort([31, 12, 31, 1, 2, 6, 3, 723, 2, 12, 3, 3, 3])
print(sorted_arr)

