  # {
  #           "reservation_id": "R123456",
  #           "guest_name": "John Doe",
  #           "room_number": 101,
  #           "room_type": "Single",
  #           "check_in": "2024-10-15",
  #           "check_out": "2024-10-18",
  #           "nights": 3,
  #           "price_per_night": 100.00,
  #           "paid": true
  #       },

# number of rooms
# number of paid reservations
# number of unpaid reservations
# total value of paid reservations
# total value of unpaid reservations

import json


room_count = 0
paid_count = 0
paid_value = 0
unpaid_count = 0
unpaid_value = 0

def readData(data):
  for reservation in data['reservations']:
    count_res(reservation)


def calc_res_value(res):
  nights = res['nights']
  price_per_night = res['price_per_night']
  total = nights * price_per_night
  return total



def is_paid(res):
  return res['paid']
    

def count_res(res):
  global room_count
  global paid_count
  global unpaid_count
  global paid_value
  global unpaid_value

  room_count += 1

  if is_paid(res):
    paid_count += 1
    paid_value += calc_res_value(res)

  else:
    unpaid_count += 1
    unpaid_value += calc_res_value(res)
  


    



with open('reservations.json', 'r', encoding='utf-8') as file:
  data = json.load(file)
  readData(data)

print('rooms', room_count)
print('paid', paid_count)
print('paid value', paid_value)
print('unpaid', unpaid_count)
print('unpaid value', unpaid_value)