def make_asterisks(num):
  output = ''
  for i in range (0, num):
    if i == 0:
      output += '*'
    else:
      output += '/*'
  return output

asterisks = make_asterisks(5)

print(asterisks)
