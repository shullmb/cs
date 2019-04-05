# Merge  Sort
from random import shuffle

arr = list(range(25))
shuffle(arr)


def merge(left, right):
    print('start of merge', left, right)
    smallest = 0
    # base cases
    if len(right) == 0:
        return left
    if len(left) == 0:
        return right
    # compare and find smallest number and remove it
    if left[0] <= right[0]:
        smallest = left.pop(0)
    else:
        smallest = right.pop(0)

    # keep merging until either list is empty
    merged = merge(left, right)
    merged.insert(0, smallest)
    print('merged', merged)
    return merged


def merge_sort(l):
    # base case
    # a list of one or fewer is considered sorted
    if len(l) <= 1:
        return l

    mid = round(len(l) / 2)
    # divide list around midpoint
    left_list = l[:mid]
    right_list = l[mid:]
    # print(left_list, right_list)
    sorted_left_list = merge_sort(left_list)
    sorted_right_list = merge_sort(right_list)
    # print(sorted_left_list, sorted_right_list)

    return merge(sorted_left_list, sorted_right_list)


merge_sort(arr)
