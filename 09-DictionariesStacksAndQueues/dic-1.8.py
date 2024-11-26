price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for key, value in price_list.items():
  print(key, value)

total_value = 0
for _,value in price_list.items():
  total_value += value
print(total_value)

for key, value in price_list.items():
  price_list[key] = round(value * 1.1, 2)

for key, value in price_list.items():
  print(key, value)

total_value = 0
for _,value in price_list.items():
  total_value += (value)
print(round(total_value))