
prev2_step = 0
prev1_step = 1

print(prev2_step)
print(prev1_step)
for i in range(2,30):
  cur_step = prev1_step + prev2_step
  print(cur_step)
  prev2_step = prev1_step
  prev1_step = cur_step
    