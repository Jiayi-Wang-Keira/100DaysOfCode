from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- random pick words ------------------------------- #
try:
    word_file = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_file = pd.read_csv("data/french_words.csv")
finally:
    word_dict = word_file.to_dict(orient="records")
random_word ={}


def random_pick():
    # random pick a word
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(word_dict)
    # french part
    canvas.itemconfig(card_image, image=card_front_image)
    french_word = random_word["French"]
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=french_word, fill="black")
    flip_timer = window.after(3000, flip_card)


def is_known():
    data = pd.DataFrame(word_dict.remove(random_word))
    data.to_csv("data/words_to_learn.csv", index=False)
    random_pick()


def flip_card():
    # english part
    canvas.itemconfig(card_image, image=card_back_image)
    english_word = random_word["English"]
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=english_word, fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# canvas
canvas = Canvas(height=526, width=800)
card_front_image = PhotoImage(file="images/card_front.gif")
card_back_image = PhotoImage(file="images/card_back.gif")
# canvas image
card_image = canvas.create_image(400, 263, image=card_front_image)
# canvas text
language_label = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 253, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button
right_image = PhotoImage(file="images/right.gif")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)
wrong_image = PhotoImage(file="images/wrong.gif")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_pick)
wrong_button.grid(row=1, column=0)

random_pick()

window.mainloop()
