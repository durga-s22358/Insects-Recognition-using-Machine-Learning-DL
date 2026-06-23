# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 13:16:44 2025
@author: Durga...
"""

import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
import re

root = tk.Tk()
root.title("Registration Form")
root.geometry("850x600")
root.config(bg="#BBD2C5")

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.StringVar()
gender = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()


db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS registration (
    Fullname TEXT,
    address TEXT,
    username TEXT UNIQUE,
    Email TEXT UNIQUE,
    Phoneno TEXT,
    Gender TEXT,
    age INTEGER,
    password TEXT
)
""")
db.commit()

def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    if (len(passwd) < 6 or len(passwd) > 20 or
        not any(char.isdigit() for char in passwd) or
        not any(char.isupper() for char in passwd) or
        not any(char.islower() for char in passwd) or
        not any(char in SpecialSym for char in passwd)):
        return False
    return True

def register():
    fname = Fullname.get().strip()
    addr = address.get().strip()
    un = username.get().strip()
    email = Email.get().strip()
    mobile = Phoneno.get().strip()
    gen = gender.get()
    ag = age.get()
    pwd = password.get()
    cnpwd = password1.get()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if fname == "" or fname.isdigit():
        ms.showerror("Error", "Enter valid full name")
    elif addr == "":
        ms.showerror("Error", "Enter address")
    elif not re.search(regex, email):
        ms.showerror("Error", "Enter a valid Email")
    elif not mobile.isdigit() or len(mobile) != 10:
        ms.showerror("Error", "Enter 10-digit mobile number")
    elif ag <= 0 or ag > 100:
        ms.showerror("Error", "Enter valid age")
    elif gen not in [1, 2]:
        ms.showerror("Error", "Select Gender")
    elif pwd == "" or not password_check(pwd):
        ms.showerror("Error", "Password must be 6-20 chars with upper, lower, number & symbol")
    elif pwd != cnpwd:
        ms.showerror("Error", "Passwords do not match")
    else:
        try:
            conn = sqlite3.connect('evaluation.db')
            cursor = conn.cursor()
            gender_val = "Male" if gen == 1 else "Female"
            cursor.execute("INSERT INTO registration (Fullname, address, username, Email, Phoneno, Gender, age, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (fname, addr, un, email, mobile, gender_val, ag, pwd))
            conn.commit()
            ms.showinfo("Success", "Account Created Successfully!")
            root.destroy()
        except sqlite3.IntegrityError as e:
            if "username" in str(e):
                ms.showerror("Error", "Username already exists")
            elif "Email" in str(e):
                ms.showerror("Error", "Email already registered")
            else:
                ms.showerror("Database Error", str(e))

form_frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=750, height=520)

tk.Label(form_frame, text="Create Your Account", font=("Helvetica", 20, "bold"), bg="white", fg="#333").grid(row=0, column=0, columnspan=4, pady=20)

fields = [
    ("Full Name", Fullname), ("Username", username),
    ("Email", Email), ("Phone Number", Phoneno),
    ("Password", password), ("Confirm Password", password1),
    ("Address", address), ("Age", age)
]

for i, (label_text, var) in enumerate(fields):
    row = (i // 2) + 1
    col = 0 if i % 2 == 0 else 2
    tk.Label(form_frame, text=label_text + ":", bg="white", font=("Arial", 11, "bold")).grid(row=row, column=col, sticky="e", padx=20, pady=10)
    entry = tk.Entry(form_frame, textvariable=var, width=25, relief="solid", bd=1, font=("Arial", 10))
    if "Password" in label_text:
        entry.config(show="*")
    entry.grid(row=row, column=col+1, padx=10, pady=10)

tk.Label(form_frame, text="Gender:", bg="white", font=("Arial", 11, "bold")).grid(row=5, column=0, sticky="e", padx=20)
tk.Radiobutton(form_frame, text="Male", variable=gender, value=1, bg="white", font=("Arial", 10)).grid(row=5, column=1, sticky="w")
tk.Radiobutton(form_frame, text="Female", variable=gender, value=2, bg="white", font=("Arial", 10)).grid(row=5, column=2, sticky="w")


def draw_gradient_button(canvas):
    canvas.create_rectangle(0, 0, 260, 45, fill="", outline="")
    canvas.create_text(130, 22, text="Register", fill="white", font=("Arial", 12, "bold"))
    canvas.bind("<Button-1>", lambda e: register())

button_canvas = tk.Canvas(form_frame, width=260, height=45, highlightthickness=0)
button_canvas.grid(row=8, column=0, columnspan=4, pady=25)

gradient = tk.PhotoImage(width=260, height=45)
r1, g1, b1 = (142, 197, 252)
r2, g2, b2 = (224, 195, 252)
for x in range(260):
    r = int(r1 + (r2 - r1) * x / 260)
    g = int(g1 + (g2 - g1) * x / 260)
    b = int(b1 + (b2 - b1) * x / 260)
    gradient.put(f"#{r:02x}{g:02x}{b:02x}", to=(x, 0, x+1, 45))

button_canvas.create_image((0, 0), image=gradient, anchor="nw")
draw_gradient_button(button_canvas)
button_canvas.image = gradient

root.mainloop()
