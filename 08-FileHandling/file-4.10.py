import csv

with open('clothing.csv') as file:
  csv_file =csv.reader(file, delimiter=',')
  next(csv_file,None)
  for row in csv_file:
    _, name, _, _, _, price, quantity = row
    if float(price) < 60 or int(quantity) < 40:
      print(row)