from random import shuffle

# arr = [84, 69, 51, 75, 83, 12, 2, 1, 11, 30, 42, 1]

arr = list(range(10000))
shuffle(arr)
print(arr)

def insertion_sort(arr):
  for i in range(1, len(arr)):
    el = arr[i]
    j = i - 1
    while j >= 0 and el < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
      arr[j + 1] = el
  print(arr)

insertion_sort(arr)