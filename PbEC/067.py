#Pattern

import turtle

turtle.shape("turtle")
for octogons in range(0, 10):
    for c in range(0, 8):
        turtle.forward(80)
        turtle.right(45)
    turtle.right(35)

turtle.exitonclick()