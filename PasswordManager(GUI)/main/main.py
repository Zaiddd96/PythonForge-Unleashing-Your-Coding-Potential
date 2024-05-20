from tkinter import *
from tkinter import messagebox
import random
import string as st
import pyperclip as pc
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    alpha = st.ascii_uppercase + st.ascii_lowercase + st.digits + st.punctuation
    length = 8
    new_password = "".join(random.sample(alpha, length))
    password.insert(0, new_password)
    pc.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_json_data = {
        website.get(): {
            "email": username.get(),
            "password": password.get()
        }
    }
    if len(website.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Field empty!", message="Please don't leave any field empty!")
    else:
        try:
            with open("password.manager.json", "r") as datafile:
                data = json.load(datafile)
        except FileNotFoundError:
            with open("password.manager.json", "w") as datafile:
                json.dump(new_json_data, datafile, indent=4)
        else:
            data.update(new_json_data)
            with open("Password.manager.json", "w") as data_file:
                json.dump(new_json_data, data_file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)


# ---------------------------- SEARCHING ------------------------------- #
def search_password():
    query = website.get()
    try:
        with open("Password.manager.json") as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File exist!")
    else:
        if query in data:
            email = data[query]["email"]
            pwd = data[query]["password"]
            messagebox.showinfo(title="Info", message=f"Email: {email}\nPassword: {pwd}")
        else:
            messagebox.showinfo(title="Oops!", message=f"no details for {query}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#0d001a")

canvas = Canvas(width=250, height=250, highlightthickness=0, bg="#0d001a")
img = PhotoImage(file="logoo.png")
canvas.create_image(125, 125, image=img)
canvas.grid(column=1, row=1)

# LABELS
website_txt = Label(text="Website:", font=("Arial", 9, "normal"), fg="#D4AF37", bg="#0d001a")
website_txt.grid(row=2, column=0)
email_txt = Label(text="Email/Username:", font=("Arial", 9, "normal"), fg="#D4AF37", bg="#0d001a")
email_txt.grid(row=3, column=0)
password_txt = Label(text="Password:", font=("Arial", 9, "normal"), fg="#D4AF37", bg="#0d001a")
password_txt.grid(row=4, column=0)

# FIELDS
website = Entry(width=36)
website.grid(column=1, row=2)
website.focus()
username = Entry(width=36)
username.grid(column=1, row=3, columnspan=1)
password = Entry(width=36)
password.grid(column=1, row=4)

# BUTTONS
generate_pass = Button(text="𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝", command=password_generator, bg="#D4AF37")
generate_pass.grid(column=2, row=4, columnspan=3)
add_info = Button(text="𝐀𝐝𝐝 𝐭𝐨 𝐌𝐚𝐧𝐚𝐠𝐞𝐫", width=36, command=save, bg="#D4AF37")
add_info.grid(column=1, row=5, columnspan=1)
search = Button(text="𝐒𝐞𝐚𝐫𝐜𝐡", command=search_password, bg="#D4AF37")
search.grid(column=2, row=2, columnspan=3)

window.mainloop()
