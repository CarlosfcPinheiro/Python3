#### Math game with functions ####
from random import randint

def addition():
    num1 = randint(5, 20)
    num2 = randint(5, 20)
    answer = int(input(f"\nSolve: {num1} + {num2} = "))
    correct = num1+num2
    add_tup = (answer, correct)
    return add_tup

def subtraction():
    num1 = randint(25, 50)
    num2 = randint(1, 25)
    answer = int(input(f"\nSolver {num1} - {num2} = "))
    correct = num1-num2
    sub_tup = (answer, correct)
    return sub_tup

def checkAnswer(answer, correct):
    if (answer == correct):
        print("Correct!")
    else:
        print(f"Wrong answer, acttualy is: {correct}")

def main():
    option = int(input("""
    [1] Addition
    [2] Subtraction
    Enter 1 or 2: """))
    match option:
        case 1:
            add_tup = addition()
            checkAnswer(add_tup[0], add_tup[1])
        case 2:
            sub_tup = subtraction()
            checkAnswer(sub_tup[0], sub_tup[1])
        case _:
            print("This option does not exist")
main()