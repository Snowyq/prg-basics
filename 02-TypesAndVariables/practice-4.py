###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170

# calculate the number of feet and inches
# feet =int( cm // 30.48)
# inches = (cm % 30.48) / 30.48 * 12

cm_to_inches = 170 / 2.54
feet = int(cm_to_inches // 12)
inches = cm_to_inches % 12



print(f'I am {cm}cm tall, i.e. {feet} feet and {round(inches,2)} inches')