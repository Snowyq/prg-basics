winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

total_hours = 0

for _, val in winter_semester.items():
  total_hours += val

print(f'The total number of hours in the winter semester is {total_hours}')