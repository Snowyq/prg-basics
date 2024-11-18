arr1 = [2,3,4,5,6,7,8,98]
arr2 = [4,6,2,98]
arr3 = [4,6,10,98]

def f(arr1,arr2):
  arr_set1 = set(arr1)
  arr_set2 = set(arr2)
  return arr_set2.issubset(arr_set1)


print(f(arr1,arr3))