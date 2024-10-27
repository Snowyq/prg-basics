def is_binary(number):
  for digit in str(number):
    if digit != '0' and digit != '1':
      return False
  return True

print(is_binary(11001010201))