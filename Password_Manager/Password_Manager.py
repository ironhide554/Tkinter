from tkinter import Tk, messagebox, Label, Button, Entry
import json
from PIL import Image, ImageTk

pw_file = "password.json"


# Functions
def save_pw():
    website = web_site.get()
    username = user_name.get()
    password = p_w.get()

    if website == "" or username == "" or password == "":
        messagebox.showerror("Invalid", "Please enter all the fields")
        return

    entry = {
        "website": website,
        "username": username,
        "password": password
    }

    try:

        f = open(pw_file, "r")
        data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)

    f = open(pw_file, "w")
    json.dump(data, f, indent=4)

    messagebox.showinfo("Success", "Password is saved successfully")

    web_site.delete(0, "end")
    user_name.delete(0, "end")
    p_w.delete(0, "end")


def clear_pw():

    clear_confirm = messagebox.askyesno("Confirm", "Are you sure to clear your all passwords?")
    if clear_confirm:
        f = open(pw_file, "w")
        f.write("[]")
        messagebox.showinfo("Success", "All the passwords are cleared successfully.")


def show_pw():
    try:
        f = open(pw_file, "r")
        data = json.load(f)
    except FileNotFoundError:
        data = []

    message = ""
    for i in data:
        website = i["website"]
        username = i["username"]
        password = i["password"]

        message += f"Website: {website}\nUsername: {username}\nPassword: {password}\n\n"

    if message == "":
        message = "No passwords found."

    messagebox.showinfo("Passwords", message)


# Creating the Window
window = Tk()
window.geometry("400x300")
window.title("Password Manager")

# Images
img = Image.open("pw.png")
image = img.resize((200, 200))
photo1 = ImageTk.PhotoImage(image)
image_label1 = Label(image=photo1)
image_label1.place(x=180, y=10)

# Credentials
website_label = Label(window, text="Website:")
username_label = Label(window, text="Username:")
pw_label = Label(window, text="Password:")

# Packing of Credentials
website_label.grid(row=0, column=0)
username_label.grid(row=1, column=0)
pw_label.grid(row=2, column=0)

# Entries
web_site = Entry(window)
user_name = Entry(window)
p_w = Entry(window,  show="*")

# Packing of entries
web_site.grid(row=0, column=1)
user_name.grid(row=1, column=1)
p_w.grid(row=2, column=1)

# Buttons
b1 = Button(window, text="Save", command=save_pw)
b2 = Button(window, text="Clear", command=clear_pw)
b3 = Button(window, text="Show Passwords", command=show_pw)

# Packing of buttons
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.place(x=30, y=100)



window.mainloop()
