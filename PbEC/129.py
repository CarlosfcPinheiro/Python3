#Check number
import tkinter

def check_Int():
    num = float(entry_num.get())
    if ((num - float(f"{num:.0f}")) == 0):
        numlist.append(int(f"{num:.0f}"))
    output_list["text"] = numlist

def reset_List():
    numlist.clear()
    output_list["text"] = ""
    
num = 0
numlist = []

window = tkinter.Tk()
window.geometry("200x200")
window.title("Check number")

#Label enter number
label_enternum = tkinter.Label(text="Enter a number")
label_enternum.place(x=40,y=20)
#Entry number
entry_num = tkinter.Entry(text=0)
entry_num.place(x=40, y=40)
#Button check
check_btn = tkinter.Button(text="Check", command= check_Int)
check_btn.place(x=50,y=70)
#Button reset
reset_btn = tkinter.Button(text="Reset", command=reset_List)
reset_btn.place(x=100,y=70)
#Output list
output_list = tkinter.Message(text="")
output_list.place(x=40, y=100,width=130,height=80)
output_list["bg"] = "white"

window.mainloop()