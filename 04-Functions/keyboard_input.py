def input_string(message):
  return input(message)

def input_integer(message):
  return int(input(message))

def input_real(message):
    return float(input(message))

def input_boolean(message):
   return True if input(message + '(y/n)') == 'y' else False


