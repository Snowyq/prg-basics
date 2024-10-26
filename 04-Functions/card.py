def hide(card_number):
  output = ''
  for index, digit in enumerate(card_number):
    if index > 1 and index < len(card_number) - 4:
      output += '*'
    else:
      output += digit
  return output