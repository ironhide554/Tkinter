from tkinter import *
import pyqrcode
from pyqrcode import QRCode
import png
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


# Functions
def on_resize(event):
    # Update widget sizes or positions based on window size changes
    pass


def makeqr():
    url = url_entry.get()

    if url=="":
        messagebox.showerror("Error", "Please provide the link.")
    else:
        url_qr = pyqrcode.create(url)
        url_qr.png("qr.png", scale=4)
        image = PhotoImage(file="qr.png")

        qr_label.config(image=image)
        qr_label.image = image
        messagebox.showinfo("Success", "Qr Code created successfully.")
        url_entry.delete(0, "end")


# GUI Window
window = Tk()
window.geometry("600x350")
window.title("QR Code Generator")

window.minsize(600, 350)
window.maxsize(600, 350)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Frames and Styling
f1 = Frame(background="black", height=1000, width=100000)
f1.place(x=0, y=0)

style = ttk.Style()
style.theme_use('xpnative')


# Labels
heading_label = Label(text="QR CODE GENERATOR", font=("algerian", 20, "bold" ), background="black", fg="green")
heading_label.grid(row=1, column=5)


url_label = Label(text="Url :", font=("georgia", 20), background="black", fg="yellow")
url_label.grid(row=2, column=4)


qr_label = Label(window, background="black")
qr_label.grid(row=5, column=5)


# Image
img_open = Image.open("qr-scan.png")
photo = img_open.resize((200, 200))
phot_img = ImageTk.PhotoImage(photo)
image_label = Label(image=phot_img,  background="black", fg="white")
image_label.grid(row=5, column=8)

# Entry
url_entry = Entry(window, font="25")
url_entry.grid(row=2, column=5)

# Button
qr_button = ttk.Button(window, text="Make QR", command=makeqr)
qr_button.grid(row=3, column=5)


window.bind('<Configure>', on_resize)

# Mainloop
window.mainloop()
