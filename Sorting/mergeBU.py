def default_compare(a, b):
  if a < b:
    return -1
  elif a > b:
    return 1
  return 0

def sort(array, compare=default_compare):
  workArray = [0] * len(array)
  chunkSize = 1

  while chunkSize < len(array):
    i = 0
    while i < len(array) - chunkSize:
      bottomUpMerge(array, i, chunkSize, workArray, compare)
      i += chunkSize * 2
    chunkSize *= 2

  return array

def bottomUpMerge(array, leftPosition, chunkSize, workArray, compare):
  rightPosition = leftPosition + chunkSize
  endPosition = min(leftPosition + chunkSize * 2 - 1, len(array) - 1)
  leftIndex = leftPosition
  rightIndex = rightPosition

  for i in range(0, endPosition - leftPosition + 1):
    if leftIndex < rightPosition and \
        (rightIndex > endPosition or \
         compare(array[leftIndex], array[rightIndex]) <= 0):
      workArray[i] = array[leftIndex]
      leftIndex += 1
    else:
      workArray[i] = array[rightIndex]
      rightIndex += 1

  for i in range(leftPosition, endPosition + 1):
    array[i] = workArray[i - leftPosition]

a = [55,23,1,6,99,32] 
b = sort(a) 
print b 

