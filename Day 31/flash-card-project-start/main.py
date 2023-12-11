from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Read data -----------------
df = pandas.read_csv("Day 31/flash-card-project-start/data/french_words.csv")
to_learn = df.to_dict(orient="records")

#generate new word----------------------
def new_word():
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

# wrong button------------
def wrong_button():
    new_word()

# right button-------------
def right_button():
    new_word()

# UI ------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526,highlightthickness=0)
cardfront_img = PhotoImage(file="Day 31/flash-card-project-start/images/card_front.png")
canvas.create_image(400, 263, image=cardfront_img)
card_title = canvas.create_text(400, 150, text="Title",font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#buttons
x_image = PhotoImage(file="Day 31/flash-card-project-start/images/wrong.png")
unknown_button = Button(image=x_image, command=wrong_button)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="Day 31/flash-card-project-start/images/right.png")
check_button = Button(image=check_image, command=right_button)
check_button.grid(row=1,column=1)

new_word()

window.mainloop()