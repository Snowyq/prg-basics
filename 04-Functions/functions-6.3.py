import month
import keyboard_input as user_input

month_num = user_input.input_integer('Enter month num (1-12): ')
month_name = month.get_name(month_num)

if month_name:
  print(f'month number {month_num} is named {month_name}')
else:
  print(f'There is no {month_num}th month')

