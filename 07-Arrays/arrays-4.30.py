arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 

for row_index, row in enumerate(arr):
  for el_index, el in enumerate(row):
    row[el_index] = ((el_index + 1) * (row_index + 1))


print(arr)