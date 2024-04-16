#Expanding ex.137 to add the credentials to a text file
import tkinter

tmp_credentials_list = []
def add_Credential():
    file = open("Credentials.txt", "a")
    name = str(name_entry.get()).title().strip()
    gender_sel = gender.get()

    newrecord = (f"{name}, {gender_sel}\n")
    tmp_credentials_list.append(newrecord)
    file.write(newrecord)
    list_credentials.insert(tkinter.END, newrecord)

    file.close()

def display_List():
    file = open("Credentials.txt", "r")
    print(file.read())
    file.close()

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
#button to display the text file in shell
display_btn = tkinter.Button(text="Display", command=display_List)
display_btn.place(x=20, y=90)
#output list
list_credentials = tkinter.Listbox()
list_credentials.place(x=150, y=60, height=120)

window.mainloop()