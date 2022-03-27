from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
logo = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_img)

logo.grid(column=1, row=0)
website_lb = Label(text="Website:")
website_lb.grid(column=0, row=1)
website_input = Entry(width=37)
website_input.grid(column=1, row=1, columnspan=2)
username_lb = Label(text="Username/Email:")
username_lb.grid(column=0, row=2)
username_input = Entry(width=37)
username_input.grid(column=1, row=2, columnspan=2)
password_lb = Label(text="Password:")
password_lb.grid(column=0, row=3)
password_input = Entry(width=20)
password_input.grid(row=3,column=1)
generate_pw_button = Button(text="Generate Password", width=14) # command
generate_pw_button.grid(row=3, column=2)
add_button = Button(text="Add", width=37)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()