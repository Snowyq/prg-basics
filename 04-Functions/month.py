months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def get_name(num): 
  if 1 <= num <= 12:
    return months[num - 1]
  else:
    return False