# <a,b> values of fib

def fib(n):
  if n == 1 or n == 0:
    return 0
  if n == 2:
    return 1
  
  return fib(n-1) + fib(n-2)

def f(a,b):
  sum = 0
  i = 0
  
  while fib(i) <= b:
    if fib(i) >= a:
      sum += fib(i)
    i += 1
    
  return sum

print(f(1,5))

# print(fib(5))
