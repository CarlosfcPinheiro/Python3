#Random pattern

import turtle
import random

turtle.shape("turtle")

lenght = random.randint(50, 250)
angle = random.randint(60, 180)
loops = random.randint(5, 365)
color = random.choice(["Blue", "Red", "Purple", "Black", "Yellow", "Green", "Brown", "Gray", "Cyan", "Orange"])

print(f"Tamanho da linha: {lenght}")
print(f"Ângulo por loop: {angle}")
print(f"Loops: {loops}")

for c in range(0, loops):
    turtle.color(color)
    turtle.forward(lenght)
    turtle.right(angle)

turtle.exitonclick()