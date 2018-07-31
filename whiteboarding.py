# the infinite parking lot

# arr of taken spaces
taken_spaces = [0,1,3]

def find_available_spot(arr):
  arr.sort()
  for i in range(len(arr)):
    if i != arr[i]:
      print(i, arr[i])
      return i
  return len(arr)

print(find_available_spot(taken_spaces))


# pig latin

def igpay_atinlay(str):
  phrase = str.split()
  new_phrase = []
  for word in phrase:
    word_arr = list(word)
    word_arr[len(word_arr-1)] = word_arr.pop(0) + 'ay'
    print(word_arr)

    

igpay_atinlay('Hello World')
