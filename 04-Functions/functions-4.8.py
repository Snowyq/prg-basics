def time_string(hours, minutes, time_format = '24'):
  output = ''
  if time_format == '12':
    fixed_hours = hours - 12 if hours > 12 else hours
    output = f'{fixed_hours:02}:{minutes:02}{'am' if hours <= 12 else 'pm'}' 
  elif time_format == '24':
    output = f'{hours:02}:{minutes:02}' 
  return output
print(time_string(13,34,'24'))