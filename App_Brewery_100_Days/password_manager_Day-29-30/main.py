import tkinter as tk
from tkinter import messagebox
import random
import pyperclip 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    mail = user_name_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {mail} "
                                                              f"\nPassword: {password} \nIs is ok to save?")

        if is_ok:
            new_entry = f"{website} | {mail} | {password}\n"
            with open("data.txt", "a") as data_file:
                data_file.write(new_entry)
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_png = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=46)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_name_label = tk.Label(text="Email/Username:")
user_name_label.grid(column=0, row=2)

user_name_entry = tk.Entry(width=46)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(0, "mail@service.com")

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = tk.Entry(width=24)
password_entry.grid(column=1, row=3)

random_button = tk.Button(text="Generate Password", command=generate_password)
random_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=47, command=save_password,  highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
