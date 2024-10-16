time_in_24 = input("Enter time (24-hour format): ")

# initialize variables
hours_in_24 = int(time_in_24[0:2])
hours_in_12 = 0

# adjusting hour 
if(hours_in_24 > 12):
  hours_in_12 =  hours_in_24 - 12

# adding zero before one digit hour
if(hours_in_12 < 10):
  hours_in_12 = str(hours_in_12).rjust(2,"0")

# combing output
time_in_12 = f"{hours_in_12}:{time_in_24[-2:]}" 

#printing output
print(f"Time in 12-hour format: {time_in_12}")


