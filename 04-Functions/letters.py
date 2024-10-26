def count_char(input_str, given_char = ''):
  if given_char == '':
    return len(input_str)

  count = 0
  for char in input_str:
    if char == given_char:
      count += 1
  return count