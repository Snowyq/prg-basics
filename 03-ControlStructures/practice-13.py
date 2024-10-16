car_speed = float(input("Enter car speed: "))

speed_limit_min = 40
speed_limit_max = 140

if car_speed > speed_limit_max or car_speed < speed_limit_min:
  print("Warning: invalid car speed!")

