temp = float(input('Enter temperature in Celsius degrees'))

if temp > 35:
  print("It is extremly hot")
elif temp > 30:
  print("It is hot")
elif temp > 15: 
  print("It is warm")
elif temp > 0:
  print("it is cold")
elif temp < 0:
  print("Warning, frost")