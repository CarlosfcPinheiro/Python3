#Name List
import tkinter


def add_Btn():
    name = str(input_name.get())
    names_list.append(name)
    output_list["text"] = names_list

def clear_Btn():
    names_list.clear()
    output_list["text"] = ""

names_list = []

window = tkinter.Tk()
window.geometry("300x400")
window.title("Name List")

#Label
text = tkinter.Label(text="Enter a name")
text.place(x=110,y=30)
#Entry_box
input_name = tkinter.Entry(text="")
input_name.place(x=100, y=50, width=100)
#Enter button
enter_btn = tkinter.Button(text="Add", command=add_Btn)
enter_btn.place(x=110,y=80)
#Clear button
clear_btn = tkinter.Button(text="Clear", command=clear_Btn)
clear_btn.place(x=150,y=80)
#Output_list
output_list = tkinter.Message(text="")
output_list.place(x=10,y=120,width=280,height=250)
output_list["bg"] = "white"

window.mainloop()

