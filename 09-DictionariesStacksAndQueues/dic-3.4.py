import queue

stack = queue.LifoQueue()


natural = 18

while natural != 0:
  reminder = natural % 2
  natural = natural // 2
  stack.put(str(reminder))

result = ''
while not stack.empty():
  result += stack.get()

print(result)