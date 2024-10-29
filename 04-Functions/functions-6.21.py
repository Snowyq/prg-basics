def f(n1,n2,n3):
  largest = n1
  smallest = n1
  for i in [n2, n3]:
    largest = largest if largest > i else i
    smallest = smallest if smallest < i else i
  return largest - smallest

print(f(10,32,20))