import queue

stack = queue.LifoQueue()

# entered = input('Enter...')

operators = ['+','*','-','/']
equal_sign = '='
def isNumber(input):
  return str(input).isnumeric()
def isOperator(input):
  return True if input in operators else False
def isEqualSign(input):
  return True if input == equal_sign else False

def calc_rpn(input):
  elements = input.split(' ')
  print(elements)
  for el in elements:
    if isNumber(el):
      stack.put(el)
    if isOperator(el):
      operator = el
      item1 = stack.get()
      item2 = stack.get()
      calculation = f'{item2} {operator} {item1}'
      stack.put(eval(calculation))
    if isEqualSign(el):
      return stack.get() if not stack.empty() else 'error'

example = '8 3 1 + / 3 2 - 4 + * ='    
print(calc_rpn(example))
