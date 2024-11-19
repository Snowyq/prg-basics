arr =[
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7]
  ]

temp_row = []
for row_i, row in enumerate(arr):
  if row_i == 0:
    for el in row:
      temp_row.append(el)
  if row_i == len(arr) - 1:
    for el_i, el in enumerate(row):
      arr[0][el_i] = el
      arr[row_i][el_i] = temp_row[el_i]

print(arr)