#Octagon

import turtle
import random

turtle.shape("turtle")

for c in range(0, 8):
    turtle.color(random.choice(["Blue", "Green", "Black", "Red", "Purple", "Yellow"]))
    turtle.forward(80)
    turtle.right(45)

turtle.exitonclick()