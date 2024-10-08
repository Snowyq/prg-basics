price = float(input('Enter price: '))
discount = float(input('Enter discount in %: '))

reduction = round(price * discount / 100)
price_after_discount =  price - reduction

print(f"Price with discount: {price_after_discount}")
print(f"Reduction : {reduction}")