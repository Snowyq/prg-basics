arr = [15,8,31,47,2,19]

mean = 0
total = 0

for index, num in enumerate(arr):
  total += num
  if index == len(arr) - 1:
    mean = total / len(arr)

print(mean)