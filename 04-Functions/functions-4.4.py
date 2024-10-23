###
# Calculates the sum of the digits in a number
#


def sum_digits(number):
    digits = str(abs(number))
    output = 0
    for digit in range(0, len(digits)):
      output += int(digits[digit])
    return output

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')