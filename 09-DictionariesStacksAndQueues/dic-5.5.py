paragraph = "cat dog mouse cat rat cat mouse"

words = paragraph.split(' ')

searched = 'cat'

words_count = {}

sum = 0
for word in words:
  if word in words_count:
    words_count[word] += 1 
  else:
    words_count[word] = 1

print(words_count)