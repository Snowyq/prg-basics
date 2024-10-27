def min_coins(amount_to_pay):
  coins = 0
  fives = amount_to_pay // 5
  coins += fives
  twos = (amount_to_pay - fives * 5) // 2
  coins += twos
  ones = amount_to_pay - fives * 5 - twos * 2
  coins += ones
  print(coins)

min_coins(23)
