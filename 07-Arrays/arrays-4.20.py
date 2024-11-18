
import MyArrays

even = []
odd = []

arr = [7,9,2,4,5,6]

for el in arr:
  even.append(el) if el % 2 == 0 else odd.append(el)

output = [*even, *odd]
print(MyArrays.arr_seperated(output))