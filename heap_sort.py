from random import shuffle

data = [0,5,100,1000,75,3,44,3490,23,4,435,123,49,403,2498]
big_data = list(range(500))
shuffle(big_data)

def heapify(arr, heap_size, index):
    big_i = index
    left_i = (index * 2) + 1
    right_i = (index * 2) + 2

    if left_i < heap_size and arr[index] < arr[left_i]:
        big_i = left_i
    
    if right_i < heap_size and arr[big_i] < arr[right_i]:
        big_i = right_i

    if big_i != index:
        arr[index],arr[big_i] = arr[big_i],arr[index]
        heapify(arr, heap_size, big_i)

def heap_sort(arr):
    heap_size = len(arr)

    for index in range(heap_size,-1, -1):
        print(arr)
        heapify(arr, heap_size, index)
    
    for index in range(heap_size - 1, 0, -1):
        arr[index],arr[0] = arr[0],arr[index]
        print(arr)
        heapify(arr, index, 0)

    return arr


print(heap_sort(data))
# print(heap_sort(big_data))