arr = [2,3,2,5,8,1,9,8]

def f(arr):
  output = []
  dic = dict.fromkeys(arr, 0)
  for num in arr:
    dic[num] += 1
  for key in dic:
    print(key)
    if dic[key] == 1:
      output.append(key)
  print(output)
  
f(arr)