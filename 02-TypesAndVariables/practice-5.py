###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('enter swift code: ')

bank_code = swift[0:4]
country_code = swift[4:6]
location_code = swift[6:8]
branch_code = swift[8:]






print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')
print(f'Location Code: {location_code}')
if(branch_code):
  print(f'Branch Code: {branch_code}')

