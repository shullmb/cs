from random import shuffle

# in place using Hoare's partition


def partition(arr, left, right):
    pivot = arr[(left+right) // 2]
    i = left
    j = right
    while True
       while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, left,right)
   if left < right:
        pivot = partition(arr, left,right)
        quick_sort(arr, left,pivot)
        quick_sort(arr, pivot + 1, right)
