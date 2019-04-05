from math import floor
from random import shuffle


def buckety_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = []
    mid = []
    right = []
    for val in arr:
        if val < pivot:
            left.append(val)
        if val > pivot:
            right.append(val)
        if val == pivot:
            mid.append(val)
    return buckety_quick_sort(left) + mid + buckety_quick_sort(right)


def bucket_sort(arr, size=10):
    buckets = [[] for bucket in range(size)]
    maximum = max(arr)
    result = []
    for num in arr:
        index = floor((num / (maximum + 1)) * size)
        buckets[index].append(num)
    for bucket in buckets:
        buckety_quick_sort(bucket)
        result = result + bucket
    return result


arr = [4, 3, 65, 85, 2, 38, 9]

print(bucket_sort(arr))
