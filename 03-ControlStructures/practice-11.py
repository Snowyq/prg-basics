curr_price = int(input("enter current price"))
old_price = int(input("enter old price"))
discount = old_price - curr_price
discount_pre = discount / old_price * 100
if curr_price < old_price * 0.9:
  print("Buy!")
print(f"discount {discount_pre}%")
