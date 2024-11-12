# 1. ["water","book","sky"]   ["water","book","sky"]
# 1. [True,False]   [True,False,True]
# 1. [5,3,1]   [5,3,1]
# 1. [3,2,1]   [3,2]

def compare(arr1, arr2):
  if len(arr1) != len(arr2):
    return False
  for index, _ in enumerate(arr1):
    if arr1[index] != arr2[index]:
      return False
  return True

print(compare([5,3,1]  , [4,3,1]))