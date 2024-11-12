arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

longest = ''

for name in arr:
  if len(name) > len(longest):
    longest = name

print(longest)