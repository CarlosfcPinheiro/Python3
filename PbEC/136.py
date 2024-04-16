#Listing name and gender
import tkinter

def add_Credential():
    name = str(name_entry.get()).title().strip()
    gender_sel = gender.get()
    newrecord = (f"{name}, {gender_sel}\n")
    list_credentials.insert(tkinter.END, newrecord)
    

window = tkinter.Tk()
window.geometry("300x200")
window.title("Listing persons")
window.wm_iconbitmap("favicon.ico")

gender = tkinter.StringVar(window)
gender.set("Gender")

#Enter name
name_entry = tkinter.Entry()
name_entry.place(x=20,y=20,width=150,height=26)
#Optionmenu gender
gender_option = tkinter.OptionMenu(window, gender, "Male", "Female")
gender_option.place(x=180,y=17)
#button add to list
add_btn = tkinter.Button(text="Add to list", command=add_Credential)
add_btn.place(x=20,y=60)
#output list
list_credentials = tkinter.Listbox()
list_credentials.place(x=150, y=60, height=120)

window.mainloop()