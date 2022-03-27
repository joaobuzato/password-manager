from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
logo = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo.create_image(100,100, image=logo_img)

logo.grid(column=1,row=1)

window.mainloop()