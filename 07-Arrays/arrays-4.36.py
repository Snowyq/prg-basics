def from_2d_to_1d(arr):
  output = []
  for row in arr:
    for el in row:
      output.append(el)
  return output

arr = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

print(from_2d_to_1d(arr))