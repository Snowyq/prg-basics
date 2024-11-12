# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
total_expenses_per_week = []
for week in monthly_expenses:
  week_exps = 0
  for exp in week:
    week_exps += exp
  total_expenses_per_week.append(week_exps)

for index, week_exp in enumerate(total_expenses_per_week):
  print(f'Week {index}:' , week_exp)

def get_inner(inner_i):
  total = 0
  for week in monthly_expenses:
      total += week[inner_i]
  return total
    

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', get_inner(0))
print('Transport:', get_inner(1))
print('Utilities:', get_inner(2))
print('Week 1:',total_expenses_per_week[0])
print('Week 2:',total_expenses_per_week[1])
print('Week 3:',total_expenses_per_week[2])
print('Week 4:',total_expenses_per_week[3])
print('---------------')
total = sum(total_expenses_per_week)
print('TOTAL', total )