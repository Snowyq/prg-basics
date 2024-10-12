###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')

phone_1of3 = phone[0:3]
phone_2of3 = phone[3:6]
phone_3of3 = phone[6:9]

formatted_phone = phone_1of3 + '-' + phone_2of3 + '-' + phone_3of3 

print(formatted_phone)
