from random import shuffle

test_array = list(range(-20, 50))
shuffle(test_array)
print('unsorted', test_array)


# Hoare's partition scheme
def partition(arr, left, right):
    pivot = arr[(left + right) // 2]
    i = left
    j = right
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr, left=0, right=None):
    if right == None:
        right = len(arr) - 1
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot)
        quicksort(arr, pivot + 1, right)

# quicksort(test_array)
# print('sorted', test_array)


def bucket_sorty_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    mid = []
    right = []

    for item in arr:
        if item < pivot:
            left.append(item)
        if item > pivot:
            right.append(item)
        elif item == pivot:
            mid.append(item)

    return bucket_sorty_quicksort(left) + mid + bucket_sorty_quicksort(right)


a_sorted = bucket_sorty_quicksort(test_array)
print('sorted', a_sorted)
