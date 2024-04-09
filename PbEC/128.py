#Km to Miles conversor
import tkinter

def convert():
    km = float(entry_km.get())
    miles = km*1.6093
    output_miles["text"] = (f"{miles:.2f} Km")

window = tkinter.Tk()
window.geometry("200x200")
window.title("Km to Miles")

#Entry km
entry_km = tkinter.Entry(text="")
entry_km.place(x=40,y=20)
#Label mile
label_mi = tkinter.Label(text="mi")
label_mi.place(x=160,y=20)
#Output miles
output_miles = tkinter.Message(text=0)
output_miles.place(x=40,y=80,width=120)
output_miles["bg"] = "white"
#Button convert
convert_Btn = tkinter.Button(text="Convert", command=convert)
convert_Btn.place(x=70,y=45)

window.mainloop()