import letters

searched_char = 'e'
string = 'You never get a second chance to make a first impression'

print(string)
print(f"The number of letter '{searched_char}': {letters.count_char(string, searched_char)}")