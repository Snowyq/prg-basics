

import draw_figures

def draw_square(length):
  # Draw a square
  for i in range(4):
    draw_figures.pen.forward(length)
    draw_figures.pen.right(90)

def draw_triangle(length):
  for i in range(3):
    draw_figures.pen.forward(length)
    draw_figures.pen.right(120)

def draw_rectangle(length_a , length_b):
  for i in range(1,5):
    if i % 2 == 0:
      draw_figures.pen.forward(length_a)
    else:
      draw_figures.pen.forward(length_b)
    draw_figures.pen.right(90)


