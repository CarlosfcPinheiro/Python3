#### Hello with a window #####
import tkinter

def sendInput():
    name = str(entry_box.get())
    output_box = tkinter.Message(text=(f"Hello, {name}!"))
    output_box.place(x=100,y=180)
    output_box["bg"] = "aqua"
    output_box["relief"] = "flat"

#### Define window's size ####
window = tkinter.Tk()
window.geometry("300x300")

#### Text mensage config ####
enter_msg = tkinter.Label(window, text = "Enter your name")
enter_msg.place(x=100,y=100)

#### Entry box ####
entry_box = tkinter.Entry(text=0)
entry_box.place(x=100,y=120)

#### Button to send the data ####
button = tkinter.Button(text="Send", command=sendInput)
button.place(x=130,y=140)

#### Loop to keep the window opened ####
window.mainloop()