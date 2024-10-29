def f(n):
  curr = 1
  prev = 0
  if n == 1:
    return 0
  if n == 2:
    return 1
  for i in range(3, n + 1):
    new = curr + prev
    prev = curr
    curr = new
    if i == n:
      return curr
    
print(f(9))