def occurs(number,arr):
  for i in arr:
    if i == number:
      return True
  return False

print(occurs(10,[2,3,4,5,1,3]))