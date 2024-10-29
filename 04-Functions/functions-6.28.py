def f(roll):
  most = "0"
  for i in range(1,7):
    curr = roll.count(str(i))
    most_roll = roll.count(most)
    if curr > most_roll:
      most = str(i)
  return most

print(f("5233165554211"))