#Manage list of names
import tkinter
import csv

def createNewFile():
    file = open("NamesTk.csv", "w")
    file.close()

def addtolist():
    file = open("NamesTk.csv", "a")
    name = str(name_entry.get())
    age = str(age_entry.get())
    newrecord = (f"{name}, {age}\n")
    file.write(newrecord)
    file.close()
    name_entry.delete(0, tkinter.END)
    age_entry.delete(0, tkinter.END)
    
def displayList():
    names_listbox.delete(0, tkinter.END)
    tmp_list = list(csv.reader(open("NamesTk.csv")))
    count = 0
    for c in tmp_list:
        names_listbox.insert(tkinter.END ,tmp_list[count])
        count+=1

window = tkinter.Tk()
window.geometry("300x300")
window.title("Manage list of names")

#Create file button
create_btn = tkinter.Button(text="New file", command=createNewFile)
create_btn.place(x=20,y=20)
#Label name and entry name
name_label = tkinter.Label(text="Enter a name:")
name_label.place(x=20,y=50)
name_entry = tkinter.Entry()
name_entry.place(x=100,y=50)
#Label age and entry age
age_label = tkinter.Label(text="Enter an age:")
age_label.place(x=20,y=80)
age_entry = tkinter.Entry()
age_entry.place(x=100,y=80,width=30)
#Add to button
addto_btn = tkinter.Button(text="Add to", command=addtolist)
addto_btn.place(x=20,y=110)
#Display list button
displaylsit_btn = tkinter.Button(text="Display", command=displayList)
displaylsit_btn.place(x=80,y=110)
#List box names
names_listbox = tkinter.Listbox()
names_listbox.place(x=20,y=140,width=100,height=140)

window.mainloop()