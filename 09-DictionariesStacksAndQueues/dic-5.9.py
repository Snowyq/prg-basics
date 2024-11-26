import csv

with open('vehicle.txt') as file:
  vehicles_lines = file.read().splitlines()

with open('province.csv', encoding='utf-8') as file:
  provinces = csv.DictReader(file, delimiter=',')
  letters = {}
  for pr in provinces:
    letters[pr['Letter']] = pr['Name']

count = 0

province_count = {}

for vehicle in vehicles_lines:
  letter = vehicle[0]
  province_name = letters[letter]
  if province_name in province_count:
    province_count[province_name] += 1
  else:
    province_count[province_name] = 1

print(province_count)