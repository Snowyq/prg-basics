import re

email_file = 'report.txt'

with open(email_file, 'r', encoding='utf-8') as file:
  content = file.read()
  f_lines = content.splitlines()
  for line_i, line in enumerate(f_lines):
     if line_i == 9:
        print(line)
  # print(f_lines[6])
  # print(f_lines[9][32])
  # print(  ord(f_lines[9][32]))

pattern = r'€(\d+)'
sum = 0
amounts = re.findall(pattern, content)
print(amounts)
for amount in amounts:
    print(amount)
    sum += int(amount)

print(sum)