from tkinter import Tk, ttk, messagebox, Label, Entry, Listbox, Button, Frame, PhotoImage, RAISED, SUNKEN, END
from typing import Any

from PIL import Image, ImageTk


expenses = []
categories = []
total_expenses = 0
budget_limit = 0


# Functions
def add_expenses():
    date = date_entry.get()
    category = category_entry.get()
    amount = float(amount_entry.get())

    if not date or not category or not amount:
        messagebox.showerror("Error", "Please enter something!!")
        return
    expenses.append((date, category, amount))
    update_expenses_lb()
    update_total_expenses()

    if category not in categories:
        categories.append(category)
        update_categories_lb()

    clear_entry()


def update_expenses_lb():
    expense_box.delete(0, END)
    for expense in expenses:
        expense_box.insert(END, expense)


def update_categories_lb():
    category_box.delete(0, END)
    for category in categories:
        category_box.insert(END, category)


def update_total_expenses():
    global total_expenses
    total_expenses = sum(expense[2] for expense in expenses)
    total_expense_value.config(text=str(total_expenses))


def set_budget_limit():
    global budget_limit
    budget_limit = float(budgetlimit_entry.get())
    if not budget_limit:
        messagebox.showerror("Error", "Please enter a budget limit!")
        return
    messagebox.showinfo("Budget Limit Set", f"Budget limit set to {budget_limit}")


def generate_report():
    report = f"Total Expenses: {total_expenses}\n"
    report += f"Budget Limit: {budget_limit}\n\n"

    if total_expenses > budget_limit:
        report += "You have exceeded your budget limit!"
    else:
        report += "You are within your budget limit."

    messagebox.showinfo("Expense Report", report)


def clear_entry():
    date_entry.delete(0, END)
    category_entry.delete(0, END)
    amount_entry.delete(0, END)


# Window of GUI
root = Tk()
root.geometry("1400x600")
root.maxsize(1400, 600)
root.title("Expense Tracker")

# Styling
style = ttk.Style()
style.theme_use('xpnative')

f1 = Frame(root, background="grey", width=2000, height=1000)
f1.place(x=0, y=0)

# Image
image = Image.open("budget.png")
i1 = image.resize((400, 400))
p1 = ImageTk.PhotoImage(i1)
photo = Label(image=p1, background="grey")
photo.place(x=1000, y=100)

# Heading
heading_label = Label(root, text="Track your expenses here!!", font=("algerian", 19, "bold"), background="black", fg="aqua")
heading_label.grid(row=0, column=1)

# Labels for entry
date_label = Label(root, text="Date: ", font=("Times New Roman", 15), background="black", fg="yellow", relief=RAISED, bd=6)
date_label.grid(row=1, column=0, padx=10, pady=10)

category_label = Label(root, text="Category: ", font=("Times New Roman", 15), background="black", fg="yellow", relief=RAISED, bd=6)
category_label.grid(row=1, column=1,  padx=10, pady=10)

amount_label = Label(root, text="Amount: ", font=("Times New Roman", 15), background="black", fg="yellow", relief=RAISED, bd=6)
amount_label.grid(row=1, column=2,  padx=10, pady=10)

# Add Expense Button
add_expense_button = ttk.Button(root, text="Add Expense", command=add_expenses)
add_expense_button.grid(row=3, column=1, pady=25)

# Labels for categories and expenses
categories_label = Label(root, text="Categories: ", font=("Times New Roman", 15), background="black", fg="yellow", relief=RAISED, bd=6)
categories_label.grid(row=4, column=0, pady=20, padx=10)

expense_label = Label(root, text="Expense: ", font=("Times New Roman", 15), background="black", fg="yellow", relief=RAISED, bd=6)
expense_label.grid(row=4, column=2, pady=10, padx=10)

# List-boxes
category_box = Listbox(root, width=30)
category_box.grid(row=5, column=0, padx=15)

expense_box = Listbox(root, width=45)
expense_box.grid(row=5, column=2)

# Budget Limit Label
budgetlimit_label = Label(root, text="Budget Limit: ", font=("Times New Roman", 15), background="black", fg="yellow", relief=RAISED, bd=6)
budgetlimit_label.grid(row=5, column=1)

budgetlimit_entry = Entry(root)
budgetlimit_entry.place(x=350, y=380)

# Set Budget Button
set_budget = ttk.Button(root, text="Set", command=set_budget_limit)
set_budget.grid(row=7, column=1, pady=20)

# Total Expense Label
total_expense_label = Label(root, text="Total Expense: ", font=("Times New Roman", 15), background="black", fg="yellow", relief=RAISED, bd=6)
total_expense_label.grid(row=8, column=0, pady=20)

total_expense_value = Label(root, text="0", font=("Times New Roman", 15), background="grey", fg="yellow")
total_expense_value.place(x=220, y=515)

# Generate Report Button
generate = ttk.Button(root, text="Generate Report", command=generate_report)
generate.grid(row=9, column=1)

# Entry of date, amount and category
date_entry = Entry(root)
date_entry.grid(row=2, column=0, padx=10)
category_entry = Entry(root, width=30)
category_entry.grid(row=2, column=1)
amount_entry = Entry(root)
amount_entry.grid(row=2, column=2)

# Running of Mainloop
root.mainloop()
