arr = [[-38, 19], [5,40],[-7,11],[29,16]]

smallest = None
sm_row = None
sm_col = None

largest = None
lg_row = None
lg_col = None


for row_i, row in enumerate(arr):
  for el_i, el in enumerate(row):
    if row_i == 0 and el_i == 0:
      smallest = el 
      largest = el
      sm_row = row_i + 1
      lg_row = row_i + 1
      sm_col = el_i + 1
      lg_col = el_i + 1
    if el < smallest:
      smallest = el
      sm_row = row_i + 1
      sm_col = el_i + 1
    if el > largest:
      largest = el
      lg_row = row_i + 1
      sm_col = el_i + 1


print(f'smallest: {smallest} row: {sm_row} col: {sm_col}')
print(f'largest: {largest} row: {lg_row} col: {lg_col}')