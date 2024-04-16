import tkinter

def check_ImageNum():
    num = str(entry_num.get())
    file_num = "assets/" + num + ".gif"
    cat_image["file"] = file_num

window = tkinter.Tk()
window.geometry("600x500")
window.title("Cat.gif")
window.wm_iconbitmap("favicon.ico")

#Label image num
label_text = tkinter.Label(text="Enter a number between 1 and 5", borderwidth=2, relief="solid")
label_text.place(x=20,y=20)
label_text["bg"] = "white"
#Entry image num
entry_num = tkinter.Entry(borderwidth=1, relief="solid")
entry_num.place(x=20,y=50,width=30)
#Send button
button_send = tkinter.Button(text="Send", command=check_ImageNum)
button_send.place(x=60,y=45)
#Image load
cat_image = tkinter.PhotoImage(file="")
image_label = tkinter.Label(image=cat_image, width=400,height=300, borderwidth=1, relief="solid")
image_label.place(x=100,y=100)

window.mainloop()