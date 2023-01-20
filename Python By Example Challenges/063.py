#Three squares

import turtle
import random

turtle.shape("turtle")

for squares in range(0, 3):
    turtle.color(random.choice(["Blue", "Red", "Green", "Purple", "Black"]))
    turtle.begin_fill()
    for square in range(0, 4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()

turtle.exitonclick()