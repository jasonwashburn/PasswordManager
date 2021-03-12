from tkinter import *
from tkinter import ttk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry = Entry(width=42)
website_entry.grid(column=1, row=1, columnspan=2)
email_user_entry = Entry(width=42)
email_user_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = ttk.Button(text="Generate Password")
generate_button.grid(column=2, row=3)
add_button = ttk.Button(text="Add", width=40)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()