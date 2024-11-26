
file_name = input('write file name: ')

try:
  with open(file_name, 'r') as file:
    content = file.read()
    file_lines = content.splitlines()
except FileExistsError:
  print('There is not such a file')

lines = 0
chars = 0
words = 0

for line in file_lines:
  lines += 1
  chars += len(line)
  line_words = line.split(' ')
  words += len(line_words)

print('lines:', lines)
print('chars:', chars)
print('words:', words)