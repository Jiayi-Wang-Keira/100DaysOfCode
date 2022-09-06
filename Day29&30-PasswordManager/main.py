from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    is_ok = False
    if website != "" and password != "":
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                          f"\nPassword: {password} \nIs it OK to save?")
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")

    if is_ok:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- Search password ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Password info", message=f"The password for {website}: {password}")
    except FileNotFoundError:
        messagebox.showwarning(message="No data File Found!")
    except KeyError:
        messagebox.showwarning(message="No details for the website exists!")
        website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# LOGO
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# LABELS
website_term = Label(text="Website:")
website_term.grid(row=1, column=0)
email_term = Label(text="Email/Username:")
email_term.grid(row=2, column=0)
password_term = Label(text="Password:")
password_term.grid(row=3, column=0)

# ENTRIES
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.insert(0, "kyawang0113@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# BUTTONS
generate_button = Button(text="Generate Password", command=password_generate, width=16)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=find_password, width=16)
search_button.grid(row=1, column=2)

window.mainloop()