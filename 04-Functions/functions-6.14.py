def calc(n1, n2, operator):
  if operator == '+':
    return n1 + n2
  elif operator == '%':
    return n1 % n2
  elif operator == '**':
    return n1 ** n2
  elif operator == '*':
    return n1 * n2
  elif operator == '-':
    return n1 - n2
  
print(calc(5,3,'*'))