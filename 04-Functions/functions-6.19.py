def f(number):
  sum = 0 
  for i in range(0,10):
    i_count = str(number).count(str(i))
    if i_count > 1:
      sum += i * i_count
  return sum

print(f(1134550))