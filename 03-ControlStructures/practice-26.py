total_pin_attemps = 3
curr_attemp = 0
pin = '1234'
is_authorized = False

while curr_attemp < total_pin_attemps:
  curr_attemp += 1
  entered_pin = input("Enter pin")
  if pin == entered_pin:
    print("pin correct")
    is_authorized = True
    break
  else:
    print("Pin incorrect")

if is_authorized:
  print("Your payment is authorized")
else:
  print("Sorry, your payment card has been blocked")


  
  