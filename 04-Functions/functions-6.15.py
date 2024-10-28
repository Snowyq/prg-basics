def people_counter(sequence):
  count = 0
  for sign in sequence:
    if sign == '+':
      count += 1
    elif sign == '-':
      count -= 1
  if count >= 3:
    return True
  else:
    return False

count = people_counter('+--++++-+')
print(count)