###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

print(f'Your speed is {car_speed}km/h')
if car_speed > speed_limit:
    print('Warning: speed limit exceeded!!')