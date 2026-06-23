# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 17:27:57 2025

@author: Durga...
"""

import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Sign-In | EV Dashboard")
root.configure(background="#E6F2FF")
root.geometry("800x550+200+50")
root.resizable(False, False)

username = tk.StringVar()
password = tk.StringVar()

def registration():
    from subprocess import call
    call(["python", "registration.py"])
    root.destroy()

def login():
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS registration
                     (Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,
                      Gender TEXT, age TEXT , password TEXT)''')
        db.commit()
        find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(username.get()), (password.get())])
        result = c.fetchall()

        if result:
            ms.showinfo("Login Success", f"Welcome, {username.get()}!")
            root.destroy()
            from subprocess import call
            call(["python", "gui_Master.py"])
        else:
            ms.showerror('Login Failed', 'Invalid Username or Password.')

title = tk.Label(
    root,
    text="🔐 Login to Your Dashboard",
    font=("Segoe UI", 26, "bold"),
    bg="#E6F2FF",
    fg="#003366"
)
title.pack(pady=40)

login_frame = tk.Frame(root, bg="white", bd=2, relief='groove')
login_frame.place(relx=0.5, rely=0.5, anchor='center', width=450, height=280)

form_title = tk.Label(
    login_frame,
    text="Please enter your credentials",
    font=("Segoe UI", 14, "italic"),
    bg="white",
    fg="#666666"
)
form_title.grid(row=0, columnspan=2, pady=20)

tk.Label(
    login_frame,
    text="👤 Username:",
    font=("Segoe UI", 14, "bold"),
    bg="white",
    anchor="w"
).grid(row=1, column=0, padx=20, pady=10, sticky="w")

txtuser = tk.Entry(login_frame, textvariable=username, font=("Segoe UI", 12), bd=2, relief="groove")
txtuser.grid(row=1, column=1, padx=20, pady=10)

tk.Label(
    login_frame,
    text="🔒 Password:",
    font=("Segoe UI", 14, "bold"),
    bg="white",
    anchor="w"
).grid(row=2, column=0, padx=20, pady=10, sticky="w")

txtpass = tk.Entry(login_frame, textvariable=password, show="*", font=("Segoe UI", 12), bd=2, relief="groove")
txtpass.grid(row=2, column=1, padx=20, pady=10)

btn_log = tk.Button(
    login_frame,
    text="➡️ Login",
    command=login,
    width=12,
    font=("Segoe UI", 12, "bold"),
    bg="#004080",
    fg="white",
    activebackground="#0059b3",
    relief='ridge',
    bd=2,
    cursor="hand2"
)
btn_log.grid(row=3, column=1, pady=20, sticky='e')

btn_reg = tk.Button(
    login_frame,
    text="📝 Register",
    command=registration,
    width=12,
    font=("Segoe UI", 12, "bold"),
    bg="#228B22",
    fg="white",
    activebackground="#2E8B57",
    relief='ridge',
    bd=2,
    cursor="hand2"
)
btn_reg.grid(row=3, column=0, pady=20, sticky='w')

# Uncomment and add your image path if needed
# img_path = 'logo.png'
# if os.path.exists(img_path):
#     logo_img = Image.open(img_path)
#     logo_img = logo_img.resize((100, 100), Image.ANTIALIAS)
#     logo = ImageTk.PhotoImage(logo_img)
#     img_label = tk.Label(root, image=logo, bg="#E6F2FF")
#     img_label.place(x=40, y=30)

root.mainloop()
