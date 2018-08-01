from random import shuffle
import math

data = [0,5,100,1000,75,3,44,3490,23,4,435,123,49,403,2498]

def get_digit(num, place, base=10):
    value = 0
    while place > 0:
        value = num % base
        num = (num - value) // base
        place -= 1
    return value

def radix_sort(arr, base=10):
    max_digits = math.trunc(math.log(max(arr), base)) + 1

    for i in range(max_digits):
        buckets = [[] for bucket in range(base)]
        for j in range(len(arr)):
            digit = get_digit(arr[j], i + 1)
            buckets[digit].append(arr[j])
            # print(buckets)
        
        index = 0
        for n in range(len(buckets) - 1):
            if buckets[n]:
                for j in range(len(buckets[n])):
                    arr[index] = buckets[n][j]
                    index += 1
                    # print('Sorting',arr)
    return arr
            
# print(get_digit(-123,2))
# print(len(data))

print('py sort', sorted(data))
print('  radix', radix_sort(data))

data = [0,5,-100,-1000,75,3,44,3490,23,4,435,123,49,403,2498]
print('py sort', sorted(data))
print('  radix', radix_sort(data))

