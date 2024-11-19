file_path = 'files.txt'

with open('files.txt', 'r') as file:
  content = file.read()
  file_lines = content.splitlines()

items_per_line = 3
file_lines_length = len(file_lines)
  
if file_lines_length > 3:
  for i in range(0, file_lines_length, items_per_line):
    new_file_lines = []
    for j in range(items_per_line):
      if i + j  < file_lines_length:
        new_file_lines.append(file_lines[i + j])
    
    with open(f'text-{int((i + items_per_line)/ items_per_line)}.txt', 'w') as file:
      for line in new_file_lines:
        file.write(line + '\n')

