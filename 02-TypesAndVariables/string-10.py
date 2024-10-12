###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in capital letters', movie.upper())

# print title in small letters
print('Title in small letters:', movie.lower())

# print how many times the vowel "e" appears in the title
print('the number of e appearance:', movie.lower().count('e'))

# print where in the text is the word "Lord"
print('position of "Lord":', movie.find('Lord'))

# print where in the text is the word "dragon"
print('position of "dragon"' , movie.find('dragon'))
