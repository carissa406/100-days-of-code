from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Read data -----------------
try:
    df = pandas.read_csv("Day 31/flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Day 31/flash-card-project-start/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


#generate new word NEXT CARD----------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill = "black")
    canvas.itemconfig(card_background, image = cardfront_img)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Day 31/flash-card-project-start/data/words_to_learn.csv", index=False)
    next_card()
    
#Flip card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text=current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image = cardback_img)

# UI ------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526,highlightthickness=0)
cardfront_img = PhotoImage(file="Day 31/flash-card-project-start/images/card_front.png")
cardback_img = PhotoImage(file="Day 31/flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=cardfront_img)
card_title = canvas.create_text(400, 150, text="Title",font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#buttons
x_image = PhotoImage(file="Day 31/flash-card-project-start/images/wrong.png")
unknown_button = Button(image=x_image, command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="Day 31/flash-card-project-start/images/right.png")
check_button = Button(image=check_image, command=is_known)
check_button.grid(row=1,column=1)

next_card()

window.mainloop()