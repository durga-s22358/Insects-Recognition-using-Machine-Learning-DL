# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 16:57:23 2025

@author: Durga...
"""

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from subprocess import call

# ========================== Main Window ==========================
root = tk.Tk()
root.title("Insect Identification System")
root.configure(background="seashell2")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")

# ========================== Background Image ==========================
bg_image = Image.open("i3.jpg").resize((w, h))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0)

# ========================== Title Label ==========================
title_text = "Insect Identification\nUsing Machine Learning and Deep Learning"
title_label = tk.Label(
    root, text=title_text,
    font=('Times New Roman', 36, 'bold'),
    bg="#012A4A", fg="white", justify="center", bd=10, relief="ridge"
)
title_label.place(x=250, y=80)

# ========================== Sub-Description ==========================
description = ("To develop a system that is capable of detecting insects\n"
               "and recommending accurate recognition using ML & DL techniques.")
desc_label = tk.Label(
    root, text=description,
    font=("Times New Roman", 20, "italic"),
    width=60, height=3,
    bg="#cce6ff", fg="black", relief="ridge", bd=5
)
desc_label.place(x=250, y=600)

# ========================== Button Function ==========================
def open_main_gui():
    call(["python", "GUI_main.py"])  # Launch main GUI

def close_app():
    root.destroy()

# ========================== Buttons ==========================
start_btn = tk.Button(
    root, text="🚀 Let's Start", command=open_main_gui,
    font=('Helvetica', 18, 'bold'), bg="#28a745", fg="white",
    activebackground="#218838", width=15, height=2, bd=4, relief="raised"
)
start_btn.place(x=600, y=300)

exit_btn = tk.Button(
    root, text="❌ Exit", command=close_app,
    font=('Helvetica', 14, 'bold'), bg="#dc3545", fg="white",
    activebackground="#c82333", width=10, height=1, bd=3
)
exit_btn.place(x=1230, y=20)

root.mainloop()
