from tkinter import *

def button_clicked():
    print("I've been clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#add padding, more space from sides of window for widgets 
window.config(padx=0, pady=20)

#label
my_label = Label(text = "I am a label", font=("Arial",24,"bold"))
#overwrites previous
my_label["text"] = "new text" #can use either one but i like the bottom better
my_label.config(text = "new text")
#my_label.pack() #side = "left"
#my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50) #add padding around specific widget

#Button
button = Button(text = "Click me", command = button_clicked)
#button.pack()
#button.place(x=100, y=9)
button.grid(column=1, row=1)

#newbutton
button2 = Button(text="New Button")
button2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
#input.pack()
#input.place(x=50, y=30)
input.grid(column=3, row=3)

#pack will pack each widget next to each other button.pack(side="right") will start from the right and continue right
#place is more precise, but kinda too specific
#grid, by columns and grids, easiest

#text
#spinbox
#scale
#checkbox
#radiobox
#listbox

#advance python arguments
#def my_function(a=1, b=2, c=3): #default arguments when u call the function later
    #do stuff
#my_function(b=5) #b is changed but the others are defaulted

#unlimited arguments
# def add(*args):
#     for n in args:
#         print(n)
# add(3, 4, 5, 6)

#unlimited keyword arguements
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs['add']
#     n *= kwargs['multiply']

# calculate(2, add=3, multiply=5)

# class Car:

#     def __init__(self, **kwargs):
#         self.make = kwargs["make"] #kwargs.get("make") - will return none if not specified later, is better
#         self.model = kwargs["model"] #kwargs.get("model")

# my_car = Car(make = "Nissan", model = "GTR")
# print(my_car.model)

#args is a tuple
#kwargs is a dictionary










window.mainloop()