with open('pets.txt', 'r') as file:
  content = file.read()
  lines = content.splitlines()
  total_words_count = 0
  for line in lines:
    words = line.split(' ')
    total_words_count += len(words)
  print(total_words_count)
