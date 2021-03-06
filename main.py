from tkinter import *
from tkinter import ttk, messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    # Check to make sure fields are filled, if not, prompt user to fix
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Field", message="Please do not leave any fields empty.")
    else:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print('data.json not found, creating new file')
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="There are no saved passwords.")
    else:
        site = data.get(website_entry.get())

        if site is not None:
            email_user_entry.delete(0, END)
            password_entry.delete(0, END)
            email_user_entry.insert(0, site['email'])
            password_entry.insert(0, site['password'])
        else:
            messagebox.showerror(title="Not Found",
                                 message=f"There is no information saved for site: {website_entry.get()}")


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Lock Background Image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=23)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_user_entry = Entry(width=42)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "wburn@wburn.net")
password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = ttk.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = ttk.Button(text="Add", width=40, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
search_button = ttk.Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
