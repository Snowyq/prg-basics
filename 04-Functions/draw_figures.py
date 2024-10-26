import turtle
import figures
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")
pen = turtle.Turtle()
pen.speed(5)

def move_pen(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

# Create the turtle

move_pen(-100, 100)
figures.draw_square(100)
move_pen(-300, 100)
figures.draw_square(50)
move_pen(100, 200)
figures.draw_triangle(50)
move_pen(100, 100)
figures.draw_triangle(100)
move_pen(100, -100)
figures.draw_rectangle(100,200)
move_pen(-100, -300)
figures.draw_rectangle(200,400)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()