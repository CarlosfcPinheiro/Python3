#Greetings
import tkinter

def output_Message():
    name = str(name_entry.get()).strip().title()
    output_msg["text"] = (f"Hello, {name}!")

window = tkinter.Tk()
window.geometry("600x500")
window.configure(background="black")
window.wm_iconbitmap("favicon.ico")
window.title("Greetings")

#import image
catimage = tkinter.PhotoImage(file="giphy.gif")
logoimage = tkinter.Label(image=catimage)
logoimage.place(x=50,y=20)

#name label
name_label = tkinter.Label(text="Enter your name: ")
name_label.place(x=50,y=350,width=120)

#enter name
name_entry = tkinter.Entry()
name_entry.place(x=180,y=350)
#Button press me
press_btn = tkinter.Button(text="Press me", command=output_Message)
press_btn.place(x=50,y=380,width=120)
#output message
output_msg = tkinter.Label(text="")
output_msg.place(x=180,y=380,width=150)


window.mainloop()