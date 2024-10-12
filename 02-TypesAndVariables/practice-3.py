###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# get temp value from keyboard
temp_in_celsius = float(input('Enter temperature in Celsius: '))

# convert from celsius to kelvin
temp_in_kelvin = temp_in_celsius + 273.15

# convert from celsius to fahrenheit
temp_in_fahrenheit = temp_in_celsius * 9 / 5 + 32

# print values
print(f'{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F')
print(f'{temp_in_celsius}°C is equal to {temp_in_kelvin}K')

