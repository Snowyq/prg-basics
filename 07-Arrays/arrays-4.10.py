arr1 = [3,36,12,28,9,44,5]
arr2 = [5,1,36]

for num1 in arr1:
  exist = False
  for num2 in arr2:
    if num1 == num2:
      exist = True
  if not exist:
    print(num1)