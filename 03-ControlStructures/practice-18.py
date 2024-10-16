x = int(input("Enter x: "))
y = int(input("Enter y: "))

point = f"P({x},{y})"
quadrant = 0
y_axis = False
x_axis = False



if x == 0:
  x_axis = True
if y == 0:
  y_axis = True

if not x_axis and not y_axis:
  if x > 0:
    if y > 0:
      quadrant = "first"
    elif y < 0:
      quadrant = "fourth"
  elif x < 0:
    if y > 0:
      quadrant = "second"
    elif y < 0:
      quadrant = "fifth"


if x_axis and y_axis:
  print(f"{point} is in center of coordinate system")
elif x_axis:
  print(f"{point} is on x axis")
elif y_axis:
  print(f"{point} is on y axis")
else:
  print(f"{point} is in {quadrant} of coordinate system")

    