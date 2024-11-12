tpl = (50,20,40,50,30,50)

def f(n):
  num = 0
  for i in tpl:
    if i == n:
      num += 1
  return num

print(f(50))
