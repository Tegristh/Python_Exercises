import tkinter as tk
import pandas as pd
import random
from tkinter import messagebox
import os

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"


# ----------------------------------- Using the csv ----------------------------------
def import_dict():
    global to_learn
    try:
        data = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv("data/bulgarian.csv")
    return data.to_dict(orient="records")


def next_card():
    global current_card
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        messagebox.showinfo(title="Error", message="No more words")
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(card_title, text="Bulgare", fill=BLACK)
    canvas.itemconfig(card_word, text=current_card['Bulgare'], fill=BLACK)
    nb_to_learn.config(text=f"words in learning list: {len(to_learn)}")
    screen.after(3000, func=reveal)


def reveal():
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(card_title, text="Français", fill=WHITE)
    canvas.itemconfig(card_word, text=current_card['Francais'], fill=WHITE)


def remove():
    global current_card, to_learn
    if len(to_learn) > 0:
        to_learn.remove(current_card)
    else:
        os.remove("data/words_to_learn.csv")
        to_learn = import_dict()

    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    # to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


to_learn = import_dict()
# ----------------------------------- Creating UI -----------------------------------
screen = tk.Tk()
screen.config(width=900, height=726, bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Flashy")

right_image = tk.PhotoImage(file="images/right.png")
wrong_image = tk.PhotoImage(file="images/wrong.png")
back_image = tk.PhotoImage(file="images/card_back.png")
front_image = tk.PhotoImage(file="images/card_front.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = tk.Button(image=right_image, highlightthickness=0, command=remove)
right_button.grid(row=1, column=1)

nb_to_learn = tk.Label(text=f"words in learning list: {len(to_learn)}", font=("Arial", 12, "bold"),
                       bg=BACKGROUND_COLOR, fg=WHITE)
nb_to_learn.grid(row=2, column=0, columnspan=2)


current_card = {}
next_card()
screen.mainloop()
