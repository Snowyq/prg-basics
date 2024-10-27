def is_negative(n1, n2, n3):
  numbers = [n1, n2, n3]
  for num in numbers:
    if num < 0:
      return True
  return False

print(is_negative(2,3,5))