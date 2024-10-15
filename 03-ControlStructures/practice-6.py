parked_hours = float(input("Enter how long car was parked (in hours!)"))
fee = 0

if parked_hours > 1 and parked_hours < 2:
  fee = 5
if parked_hours > 3 and parked_hours < 6:
  fee = 15
if parked_hours > 6:
  fee = 20

print("Fee for paring", fee)