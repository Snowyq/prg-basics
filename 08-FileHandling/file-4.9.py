import csv

with open('it_company.csv') as file:
  rows = csv.reader(file,delimiter=',')
  for row in rows: 
    last_name,first_name, job,email = row
    if job == 'Graphic Designer':
      print(f'{first_name} {last_name}, {email}')