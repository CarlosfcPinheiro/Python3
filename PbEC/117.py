#Quizscore
import csv
from random import randint

name = str(input("Enter your name: ").strip().title())
score = 0
resps = []

for c in range(0, 2):
    num1 = randint(10,50)
    num2 = randint(10, 50)
    answer_sum = int(input(f"Solve: {num1} + {num2} = "))
    resps.append(answer_sum)
    if (answer_sum == num1+num2):
        score += 1

file = open("Quizscore.csv", "a")
newrecord = (f"{name}, {resps[0]}, {resps[1]}, {score}\n")
file.write(newrecord)