arr =[
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7]
  ]

temp = 0

for row in arr:
  for el_i, el in enumerate(row):
    if el_i == 0:
      temp = el
    if el_i == len(row) - 1:
      row[0] = el
      row[el_i] = temp
      

print(arr)
