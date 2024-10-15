###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input('Enter first number'))
number2 = float(input('Enter second number'))
operator = input('Enter operator')
result = 0

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 == 0:
      print("You can't divide by 0")
    else:
      result = number1 / number2

# print result
if(result):
  print(f'{number1} {operator} {number2} = {result}')