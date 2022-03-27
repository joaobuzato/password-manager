from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save(website, username, password):
    with open("data.txt", "a") as file:
        file.write(f"{website} | {username} | {password} \n")
        website_input.delete(0, 'end')
        password_input.delete(0, 'end')


def validate():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if website is None or username is None or password is None:
        print("All of the fields must be filled!")
    else:
        save(website, username, password)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_img)

logo.grid(column=1, row=0)
website_lb = Label(text="Website:")
website_lb.grid(column=0, row=1)
website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
username_lb = Label(text="Username/Email:")
username_lb.grid(column=0, row=2)
username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "joaobuzato@gmail.com")
password_lb = Label(text="Password:")
password_lb.grid(column=0, row=3)
password_input = Entry(width=20)
password_input.grid(row=3,column=1)
generate_pw_button = Button(text="Generate Password", width=16) # command
generate_pw_button.grid(row=3, column=2)
add_button = Button(text="Add", width=37, command=validate)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()