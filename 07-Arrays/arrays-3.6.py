arr = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i,inner_arr in enumerate(arr):
  arr[i][i] =1 
  for j, _ in enumerate(inner_arr):
    print(arr[i][j], end=' ')
  print()

