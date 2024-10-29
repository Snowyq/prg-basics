def f(palindrome):
  reversed = ''
  for char in palindrome:
    reversed = char + reversed
  
  if reversed == palindrome:
    return True
  else:
    return False
  

  # arr = palindrome.split()
  # arr.reverse()
  # reversed = ''.join(arr)
  # return reversed

print(f('kajak'))