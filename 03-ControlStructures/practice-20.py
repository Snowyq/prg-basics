decimal_num = int(input("Enter decimal number"))
is_done = False
cache_num = decimal_num
remainder = 0

output = ""

while not is_done:
  curr_num = cache_num
  cache_num = curr_num // 2
  remainder = curr_num % 2

  if not curr_num == 0:
    output = str(remainder) + output
  else:
    is_done = True

print(output)

