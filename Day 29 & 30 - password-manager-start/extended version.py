from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    web_entry = website_input.get()
    gmail_entry = gmail_input.get()
    pass_entry = password_input.get()
    web_pass = {
        web_entry: {
            "email": gmail_entry,
            "password": pass_entry
        }
    }
    if len(web_entry) > 0 and len(pass_entry) > 0:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(web_pass, data_file, indent=4)
        else:
            data.update(web_pass)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showinfo(title="Warning", message="Dont leave any box empty")
# ---------------------------- PASSWORD SEARCH ------------------------------- #


def find_password():
    web_entry = website_input.get()
    try:
        with open("data.json", "r") as data_fie:
            data = json.load(data_fie)
            try:
                search_result = data[web_entry]
            except KeyError:
                messagebox.showinfo(title="New Entry", message="No details for the website exists")
            else:
                messagebox.showinfo(title="Details exist", message=f"Email: {data[web_entry]['email']}\nPassWord: {data[web_entry]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="New Data", message="Data file Found")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("PassWord Manager")
window.config(padx=50, pady=50)

lock = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

heading1 = Label(text="Website:")
heading1.grid(row=1, column=0)
heading2 = Label(text="Email/Username:")
heading2.grid(row=2, column=0)
heading3 = Label(text="Password:")
heading3.grid(row=3, column=0)

website_input = Entry(width=32)
website_input.grid(row=1, column=1)
website_input.focus()
gmail_input = Entry(width=51)
gmail_input.grid(row=2, column=1, columnspan=2)
gmail_input.insert(0, "ghost@gmail.com")
password_input = Entry(width=32)
password_input.grid(row=3, column=1)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password", command=generate_pass, width=15)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()