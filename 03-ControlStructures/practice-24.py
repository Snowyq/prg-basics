
for i in range(9):
  stars_num = 0
  outcome = ""

  if i < 5:
    stars_num = i + 1
  else: 
    stars_num = 9 - i

  for j in range(stars_num) :
    outcome += '*'
  print(outcome)