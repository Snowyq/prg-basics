def bubble_sort(arr):
  for i in range(0, len(arr)):
    for j in range(0,len(arr)-i-2):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
  return arr

  
print(bubble_sort([2,3,1,1,5]))