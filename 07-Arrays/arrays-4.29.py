def create_2d_array(x,y):
  arr = []
  for _ in range(x):
    row = []
    for _ in range(y):
      row.append(0)
    arr.append(row)
  return arr

print(create_2d_array(3,5))