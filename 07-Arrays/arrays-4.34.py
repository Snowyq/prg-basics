def identity_matrix(n):
  arr = []
  for i in range(n):
    row = []
    for j in range(n):
      row.append(1) if j == i else row.append(0) 
    arr.append(row)
  return arr

print(identity_matrix(3))
print(identity_matrix(5))
print(identity_matrix(8))
