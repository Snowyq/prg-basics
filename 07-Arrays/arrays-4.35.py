def transpose_matrix(m):
  transposed_m = [[0] * len(m) for _ in range(len(m[0]))]
  for row_i, row in enumerate(m):
    for el_i, el in enumerate(row):
      transposed_m[el_i][row_i] = el
  return transposed_m

arr = [
  [1, 2, 3],
  [4, 5, 6],
  # [7, 8, 9]
]

print(transpose_matrix(arr))