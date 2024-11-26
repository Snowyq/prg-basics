import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct
brackets_start = ['{','[','(']
brackets_end = ['}',']',')']

def brackets_ok(expression):
  brackets_stack = queue.LifoQueue()
  for char in expression:
      if char in brackets_start:
        brackets_stack.put(char)
      if char in brackets_end:
         last_opened = brackets_stack.get()
         if brackets_end.index(char) != brackets_start.index(last_opened):
            return False
  return brackets_stack.empty()


print(brackets_ok(expression1))
print(brackets_ok(expression2))
print(brackets_ok(expression3))
# if brackets_ok(expression1):
#    print(...)
# else
#    ...

# if brackets_ok(expression2):
# ...
# ...