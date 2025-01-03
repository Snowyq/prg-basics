``###
# Prints some array elements
#


import math

arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last value', arr[len(arr) - 1])
print('Sum last and first value', arr[-1] + arr[0])
print('Middle value', arr[math.floor(len(arr)/2)])

output = ''
for i in arr:
  if i > 0:
    output+=' '
  output += str(i)
print(output)