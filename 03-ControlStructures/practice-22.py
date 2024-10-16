for num in range(1,31):
  is_by_5 = bool(num % 5 == 0)
  is_by_3 = bool(num % 3 == 0)

  if is_by_3 and is_by_5:
    print("BINGO")
  elif is_by_5:
    print("FIVE")
  elif is_by_3:
    print("THREE")
  else:
    print(num)