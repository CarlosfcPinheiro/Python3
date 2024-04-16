#Math quiz
import tkinter
from random import randint

list_nums = ()
def random_Num():
    while True:
        num1 = randint(10, 50)
        num2 = randint(10, 50)

        if (num1 == num2):
            continue
        else:
            break
    tmp_nums_lsit = (num1, num2)
    return tmp_nums_lsit

def check_Answer():
    answer = int(answer_entry.get())
    answer_entry.delete(0, tkinter.END)
    correct_label["bg"] = "gray"
    if (answer == correctanswer):
        correct_label["text"] = "Correct!"
        create_NextBtn()
    else:
        correct_label["text"] = "Wrong..."
        create_NextBtn()

def new_Numbers():
    list_nums = random_Num()
    correctanswer = list_nums[0] + list_nums[1]
    question_label["text"] = (f"{list_nums[0]} + {list_nums[1]} = ")

#storing variables
list_nums = random_Num()
correctanswer = list_nums[0] + list_nums[1]
    
window = tkinter.Tk()
window.geometry("500x300")
window.wm_iconbitmap("favicon.ico")
window.configure(background="white")
window.title("Sum Numbers")

#Label explanation
explanation_label = tkinter.Label(text="Solve and enter the correct answer")
explanation_label.place(x=20,y=20,width=460)
#Label question
question_label = tkinter.Label(text=(f"{list_nums[0]} + {list_nums[1]} = "))
question_label.place(x=200,y=60)
#Entry answer
answer_entry = tkinter.Entry()
answer_entry.place(x=260,y=60,width=20)
#check answer button
checkanswer_btn = tkinter.Button(text="Enter Answer", command=check_Answer)
checkanswer_btn.place(x=200,y=90)
#Label answer output
correct_label = tkinter.Label(text="")
correct_label.place(x=220,y=200)
correct_label["bg"] = "white"

def create_NextBtn():
    #Next button
    next_button = tkinter.Button(text="Next", command=new_Numbers)
    next_button.place(x=225,y=230)

window.mainloop()