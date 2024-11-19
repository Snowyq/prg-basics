def words_count(sentence):
  return len(sentence.split(' '))

def by_word_length(arr):
  return sorted(arr,key= len, reverse=True)

def by_alph(arr):
  return sorted(arr)