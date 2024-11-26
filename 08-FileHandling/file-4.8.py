with open('files.txt', 'r') as file:
  content = file.read()
  file_lines = content.splitlines()

files = []
for line in file_lines:
  _, ext = line.split('.')
  if len(ext) == 4:
    files.append(line)

print(files)