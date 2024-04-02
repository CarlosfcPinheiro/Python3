#### Guess the number ####
from random import randint

def genNumber():
    hnum = int(input("Enter a high number: "))
    lnum = int(input("Enter a low number: "))
    comp_num = randint(lnum, hnum)
    return comp_num

def guessNum():
    guess = int(input("I am thinking of a number... Try to guess: "))
    return guess

def checkNum():
    randnum = genNumber()
    while True:
        guessnum = guessNum()
        if (guessnum == randnum):
            print("\nCorrect! You win.")
            break
        else:
            if (guessnum < randnum):
                print(f"\nThe number is upper than {guessnum}")
                continue
            else:
                print(f"\nThe number is less than {guessnum}")
                continue
checkNum()