def sum_of_digits(number, set_to_even):
  sum = 0
  for digit in str(number):
    is_even = int(digit) % 2 == 0
    if set_to_even:
      sum += int(digit) if is_even else 0
    else:
      sum += int(digit) if not is_even else 0
  return sum

sum = sum_of_digits(33240, True)
print(sum)
    
