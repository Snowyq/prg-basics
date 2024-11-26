import queue
stack = queue.LifoQueue()

def f(input):
  for char in input:
    stack.put(char)
  output = ''
  while not stack.empty():
    output += stack.get()
  return output

print(f('jakub'))