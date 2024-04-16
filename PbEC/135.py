#Colors
import tkinter

def change_Color():
    sel = select.get()
    window.configure(background=sel)

window = tkinter.Tk()
window.geometry("200x200")
window.title("Colors")
window.wm_iconbitmap("favicon.ico")

select = tkinter.StringVar(window)
select.set("white")

#List colors
list_colors = tkinter.OptionMenu(window, select, "yellow", "blue", "light blue", "red", "gray", "white", "black")
list_colors.place(x=20,y=50, width=80, height=80)
#Button change background
change_btn = tkinter.Button(text="Select", command=change_Color)
change_btn.place(x=110, y=80)

window.mainloop()