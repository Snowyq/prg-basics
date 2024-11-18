
greater_than = int(input('Enter value: '))

def find_greater(arr, val):
  return filter(lambda el: el> val, arr)


print(', '.join(map(lambda el: str(el),find_greater([2,34,1,5,2,412,43,5],greater_than))))