def negative_even_count(start_range, _):
  count = 0
  for i in range(start_range, 0):
    is_even = i % 2 == 0
    if is_even:
      count += 1  
  return count



count = negative_even_count(-10,5)
print(count)
