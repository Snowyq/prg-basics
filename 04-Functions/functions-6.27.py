def f(product_code):
  sum = 0
  for i , char in enumerate(product_code):
    if i < 3:
      sum += int(char)
    elif i == 3:
      if sum % 7 == int(char):
        return True
      else:
        return False

print(f("1082"))