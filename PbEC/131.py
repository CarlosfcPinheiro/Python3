import tkinter
import csv

def create_File():
    file = open("NamesTk.csv", "w")
    file.close()

def addto_CurrentF():
    name = str(name_entry.get())
    age = int(age_entry.get())
    age_entry.delete(0, tkinter.END)
    name_entry.delete(0, tkinter.END)
    newrecord = (f"{name}, {age}\n")
    file = open("NamesTk.csv", "a")
    file.write(newrecord)
    file.close()

window = tkinter.Tk()
window.geometry("300x200")
window.title("Manage csv")

#Button create file
create_btn = tkinter.Button(text="Create new", command=create_File)
create_btn.place(x=20,y=20)
#Entry name
name_label = tkinter.Label(text="Enter a name")
name_label.place(x=20,y=50)
name_entry = tkinter.Entry()
name_entry.place(x=100,y=50)
#Entry age
age_label = tkinter.Label(text="Enter age")
age_label.place(x=20,y=80)
age_entry = tkinter.Entry()
age_entry.place(x=80,y=80,width=30)
#Button to add in the end of the list
add_btn = tkinter.Button(text="Add to the file", command=addto_CurrentF)
add_btn.place(x=20,y=110)

window.mainloop()