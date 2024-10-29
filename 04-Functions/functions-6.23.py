def f(password):
  is_diff = True
  for char in password:
    if password.count(char) > 1:
      is_diff = False
      break
  if len(password) >= 6 and is_diff:
    return True
  else:
    return False
  
print(f('haslog1'))