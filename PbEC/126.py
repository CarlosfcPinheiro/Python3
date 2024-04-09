#Adding bumbers
import tkinter

def add_to():
    num = int(entry_box.get())
    answer = int(output_box["text"])
    total = num + answer
    output_box["text"] = total

def reset():
    total = 0
    output_box["text"] = 0
    entry_box.delete(0, num)

num = 0
total = 0

#window
window = tkinter.Tk()
window.geometry("300x200")
window.title("Adding unities")

#Label Message
label = tkinter.Label(text="Click on the button to add in the total or reset it.")
label.place(x=20,y=20)

#Entrybox input
entry_box = tkinter.Entry(text="")
entry_box.place(x=90,y=60)
#Entrybox output
output_box = tkinter.Message(text=0)
output_box.place(x=100,y=90, width=100)
output_box["bg"]="white"

#Buttons
button_add = tkinter.Button(text="Add 1", command=add_to)
button_add.place(x=100,y=120)
button_reset = tkinter.Button(text="Reset", command=reset)
button_reset.place(x=150,y=120)

window.mainloop()