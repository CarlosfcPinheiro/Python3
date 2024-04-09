#### Rolling a dice ####
import tkinter
from random import randint

def roll_Dice():
    num = randint(1, 6)
    output_box = tkinter.Message(text=(f"The number is: {num}"))
    output_box.place(x=130,y=160)
    output_box["bg"] = "white"

def main():
    #window
    window = tkinter.Tk()
    window.geometry("350x300")

    #button to roll the dice
    button_roll = tkinter.Button(text="Roll", command=roll_Dice)
    button_roll.place(x=150,y=125)

    window.mainloop()

main()