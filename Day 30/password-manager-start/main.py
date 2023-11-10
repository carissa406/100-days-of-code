from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def gen_pass():
    pass_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _  in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(END, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get()
    email = user_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }

    if len(website_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("Day 30\password-manager-start\data.json", mode ='r') as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("Day 30\password-manager-start\data.json", mode = 'w') as data_file:
                json.dump(data, data_file,indent=4)
        else:
            data.update(new_data)
            with open("Day 30\password-manager-start\data.json", mode = 'w') as data_file:
                json.dump(data, data_file,indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        with open("Day 30\password-manager-start\data.json", mode ='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Not Found', message='No Data File Found')
    else:
        if website_entry.get() in data:
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {data[website_entry.get()]['email']} \nPassword: {data[website_entry.get()]['password']}")
        else:
            messagebox.showinfo(title=website_entry.get(), message='No details for the website exists')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height = 200, width = 200, highlightthickness=0)
tomato_img = PhotoImage(file="Day 29\password-manager-start\logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0,row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

#entry
website_entry = Entry(width=35)
website_entry.grid(column=1,row=1, columnspan=2, sticky="EW")
website_entry.focus()

user_entry = Entry(width=35)
user_entry.insert(END, string="hicks.carissa@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3, sticky="EW")

#buttons
gen_pass_button = Button(text="Generate Password", command=gen_pass)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(column=1,row=4,columnspan=2, sticky="EW")

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")














window.mainloop()