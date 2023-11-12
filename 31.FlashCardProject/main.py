# FRENCH FLASH CARD

from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def word_change():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=french_card)
    flip_timer = window.after(3000, func=flip_card)


def know_word():
    to_learn.remove(current_card)
    data_write = pd.DataFrame(to_learn)
    data_write.to_csv("data/words_to_learn.csv", index=False)
    word_change()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=english_card)


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)
# French card
canvas = Canvas(width=800, height=526)
french_card = PhotoImage(file=".\\images\\card_front.png")
english_card = PhotoImage(file=".\\images\\card_back.png")
card_bg = canvas.create_image(400, 263, image=french_card)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0, background=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Wrong button
wrong_img = PhotoImage(file=".\\images\\wrong.png")
button = Button(image=wrong_img, highlightthickness=0, command=word_change)
button.grid(row=1, column=0)

# Right button
right_img = PhotoImage(file=".\\images\\right.png")
button = Button(image=right_img, highlightthickness=0, command=know_word)
button.grid(row=1, column=1)

# Calling function so automatically a title and word gets picked up
word_change()

window.mainloop()
