###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"

words = university.split()
abbrevation = ''

for word in words: 
  if word[0].isupper():
    abbrevation += word[0]
  

print(f"abbrevation of {university}: {abbrevation}")