import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# --------------------------- SEARCH ----------------------------

def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Ooops...", message="No Data File Found")
    else:
        credentials = data.get(website)
        if credentials is not None:
            messagebox.showinfo(title=website, message=f"username: {credentials.get('username')} \npassword: {credentials.get('password')}")
        else:
            messagebox.showinfo(title="Ooops...", message="This website is not saved.")

# ---------------------------- PASSWORD GENERATOR -------------------------------
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0,END)
    password_input.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password copied", message="Your Password is already copied to the clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save(new_data):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)


def validate():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) ==0:
        messagebox.showinfo(title="Ooops...", message="Hey, you left some fields empty")
    else:
        if messagebox.askokcancel(title=website, message=f"Are you fine with this details? \n {username} \n {password}"):
            new_data ={
                website:{
                    "username": username,
                    "password": password
                }
            }
            save(new_data)
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
website_input = Entry(width=20)
website_input.grid(column=1, row=1)
search_button = Button(text="Search", command=search, width=16)
search_button.grid(row=1, column=2)
website_input.focus()
username_lb = Label(text="Username/Email:")
username_lb.grid(column=0, row=2)
username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "joaobuzato@gmail.com")
password_lb = Label(text="Password:")
password_lb.grid(column=0, row=3)
password_input = Entry(width=20)
password_input.grid(row=3, column=1)
generate_pw_button = Button(text="Generate Password", width=16, command=generate_password)
generate_pw_button.grid(row=3, column=2)
add_button = Button(text="Add", width=37, command=validate)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()