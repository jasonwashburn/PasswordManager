from tkinter import *
from tkinter import ttk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


# Lock Background Image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=1)

window.mainloop()