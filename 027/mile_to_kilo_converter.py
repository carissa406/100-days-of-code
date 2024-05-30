from tkinter import *

def button_clicked():
    label3 = Label(text=calculate(input))
    label3.grid(column=2, row = 1)

def calculate(input):
    user_input = input.get()
    answer = str(float(user_input) * 1.6)
    return answer

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

label1 = Label(text = "is equal to")
label1.grid(column=0, row = 1)

input = Entry()
input.grid(column=2, row=0)

label2 = Label(text="Miles")
label2.grid(column=3, row=0)

button = Button(text = "Calculate", command=button_clicked)
button.grid(column=2,row=2)

window.mainloop()