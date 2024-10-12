###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Anna'   # replace Anna with your name
surname = 'May' # replace May with your surname
fullname = name + ' ' + surname

characters_in_name = len(name)
characters_in_surname = len(surname)
characters_in_fullname = len(fullname)


print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_fullname} characters') # with a space between name and surname

