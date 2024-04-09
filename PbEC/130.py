#Save into a csv file
import csv
import tkinter

def check_Int():
    num = float(entry_num.get())
    if ((num - float(f"{num:.0f}")) == 0):
        num_list.insert(tkinter.END, int(num))
        entry_num.delete(0, tkinter.END)
    else:
        entry_num.delete(0, tkinter.END)

def reset_List():
    num_list.delete(0, tkinter.END)
    entry_num.focus()

def save_List():
    file = open("NumbersTk.csv", "w")
    tmp_list = num_list.get(0, tkinter.END)
    count = 0
    for c in tmp_list:
        newrecord = (f"{tmp_list[count]}\n")
        file.write(newrecord)
        count += 1
    file.close()

num = 0
window = tkinter.Tk()
window.geometry("200x200")

#Label enter number
label_enternum = tkinter.Label(text="Enter a number")
label_enternum.place(x=40,y=20)
#Entry number
entry_num = tkinter.Entry(text=0)
entry_num.place(x=40, y=40)
#Button check
check_btn = tkinter.Button(text="Check", command= check_Int)
check_btn.place(x=40,y=70)
#Button reset
reset_btn = tkinter.Button(text="Reset", command=reset_List)
reset_btn.place(x=90,y=70)
#Button save in csv
save_btn = tkinter.Button(text="Save", command=save_List)
save_btn.place(x=135,y=70)
#Numlist output
num_list = tkinter.Listbox()
num_list.place(x=40, y=100,width=130,height=80)
num_list["bg"] = "white"

window.mainloop()