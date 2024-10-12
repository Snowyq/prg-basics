###
# Calculation of circle area and circumference 
#
import math


# determine radius and PI values
# radius = int(input('enter circle radius:'))

radius = 5

if(radius > 0):
# calculate area 
  area = radius**2 * math.pi
# calculate circumference 
  circumference = 2 * radius * math.pi
# print results
  print(f'r = {radius} --> circumference = {round(circumference,2)}, area = {round(area,2)}')
else:
  print('You have entered non positive radius!')

