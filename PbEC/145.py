import sqlite3
import tkinter

def add_Btn():
    name = str(entry_name.get())
    grade = int(entry_grade.get())
    cursor.execute("""INSERT INTO scores(Name, Score) VALUES(?, ?)""", (name, grade))
    db.commit()

    entry_name.delete(0, tkinter.END)
    entry_grade.delete(0, tkinter.END)

def clear_Btn():
    entry_grade.delete(0, tkinter.END)
    entry_name.delete(0, tkinter.END)

#Create DB
with sqlite3.connect("TestScores.db") as db:
        cursor = db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS scores(
    ID integer PRIMARY KEY,
    Name text NOT NULL,
    Score integer NOT NULL);""")

#Create interface
window = tkinter.Tk()
window.geometry("300x200")
window.title("Students DB")

label_name = tkinter.Label(text="Enter student's name: ")
label_name.place(x=10,y=20)
entry_name = tkinter.Entry()
entry_name.place(x=138,y=21)

label_grade = tkinter.Label(text="Enter student's grade: ")
label_grade.place(x=10, y=50)
entry_grade = tkinter.Entry()
entry_grade.place(x=138,y=51)

button_add = tkinter.Button(text="Add", command=add_Btn)
button_add.place(x=75,y=100, width=60)

button_clear = tkinter.Button(text="Clear", command=clear_Btn)
button_clear.place(x=155,y=100, width=60)

window.mainloop()
db.close()
