# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 16:44:51 2025

@author: Durga...
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import sqlite3
#import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("MAIN PAGE")



#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('i5.png')
image2 =image2.resize((1400,800))

background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="'A vision model trained for insect recognition \n uses deep learning to identify insects from images.'", font=('Times New Roman', 35,' bold '),bg="#013220",fg="white")
lbl.place(x=200, y=0)


def reg():
    from subprocess import call
    call(["python","GUI_Master_old.py"])






button1 = tk.Button(root, text="Detection", command=reg, width=12, height=1,font=('times', 20, ' bold '), bg="#0909FF", fg="#FFFFFF")
button1.place(x=650, y=350)



root.mainloop()