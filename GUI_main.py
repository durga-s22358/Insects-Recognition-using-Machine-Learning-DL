# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 16:44:51 2025

@author: Durga...
"""


import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os#####+======
import numpy as np
import time

global fn
fn = ""
#########################################=======================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")

 
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Vision Model Trained To Recognize Insects.")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('i8.jpg')
image2 = image2.resize((1350,650), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=70)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="'Insect Identification\nUsing Machine Learning and Deep Learning'",font=("Times New Roman", 28, 'bold'),
                    background="#152238", fg="white", width=70, height=2)
label_l1.place(x=0, y=0)




#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Sign-IN", command=log, width=12, height=1,font=('times', 20, ' bold '), bg="#0909FF", fg="#FFFFFF")
button1.place(x=650, y=100)

button2 = tk.Button(root, text="Sign-UP",command=reg,width=12, height=1,font=('times', 20, ' bold '), bg="#008000", fg="#FFFFFF")
button2.place(x=870, y=100)

button3 = tk.Button(root, text="Exit",command=window,width=12, height=1,font=('times', 20, ' bold '), bg="brown", fg="#FFFFFF")
button3.place(x=1100, y=100)

root.mainloop()