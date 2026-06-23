# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 16:44:51 2025

@author: Durga...
"""

import tkinter as tk
from tkinter import ttk, LEFT
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import numpy as np
import cv2
import time
import VITModel
from tensorflow.keras.models import load_model

global fn
fn = ""

# Class labels (update as needed)
class_labels = ['Butterfly', 'Dragonfly', 'Grasshopper', 'Ladybug', 'Mosquito']

# ========================== MAIN WINDOW ==========================
root = tk.Tk()
root.title(" Insects Recognition using Machine Learning")
root.configure(background="#1e1e2f")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")

# ========================== HEADING LABEL ==========================
heading = tk.Label(
    root,
    text="🧠 Insects Recognition using Machine Learning & Deep Learning",
    font=('Helvetica', 24, 'bold'),
    bg="#2c2f33",
    fg="white",
    pady=20
)
heading.pack(fill="x")

# ========================== SIDE FRAME ==========================
frame_controls = tk.LabelFrame(
    root, text="Operations Panel", width=250, height=400,
    font=('Helvetica', 14, 'bold'), bg="#77dd77", fg="black", bd=4
)
frame_controls.place(x=20, y=150)

# ========================== IMAGE PANEL ==========================
image_label = tk.Label(root, bg="#1e1e2f")
image_label.place(x=300, y=150)

# ========================== RESULT LABEL ==========================
result_label = tk.Label(
    root, text="", width=50,
    font=('Helvetica', 18, 'bold'),
    bg='#d1e231', fg='black'
)
result_label.place(x=300, y=500)

# ========================== UPDATE LABEL ==========================
def update_label(message):
    result_label.config(text=message)

# ========================== OPEN IMAGE ==========================
def openimage():
    global fn
    fileName = askopenfilename(
        initialdir='D:/Protech Solutions all data/New Project 2025-26/Convolutional Neural Network (CNN)/Insects Recognition/Testing_set',
        title='Select image for Analysis',
        filetypes=[("All files", "*.*")]
    )
    fn = fileName
    img = Image.open(fn).resize((200, 200))
    imgtk = ImageTk.PhotoImage(img)
    image_label.config(image=imgtk)
    image_label.image = imgtk

# ========================== IMAGE PREPROCESSING ==========================
def convert_grey():
    global fn
    if not fn:
        update_label("Please select an image first!")
        return

    img = cv2.imread(fn)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    gray_img = ImageTk.PhotoImage(Image.fromarray(gray).resize((200, 200)))
    binary_img = ImageTk.PhotoImage(Image.fromarray(thresh).resize((200, 200)))

    gray_label = tk.Label(root, text="Gray", font=('Helvetica', 14, 'bold'), image=gray_img, compound="bottom", bg="#eeeeee")
    gray_label.image = gray_img
    gray_label.place(x=550, y=150)

    binary_label = tk.Label(root, text="Binary", font=('Helvetica', 14, 'bold'), image=binary_img, compound="bottom", bg="#eeeeee")
    binary_label.image = binary_img
    binary_label.place(x=800, y=150)

# ========================== CNN PREDICTION ==========================
def test_model_proc(image_path):
    model = load_model("Insects_model.h5")
    img = Image.open(image_path).resize((64, 64))
    img_array = np.array(img).astype('float32') / 255.0
    img_array = img_array.reshape(1, 64, 64, 3)
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    return class_labels[class_index]

def test_model():
    global fn
    if not fn:
        update_label("Please select an image!")
        return

    update_label("Model is predicting...")

    start = time.time()
    result = test_model_proc(fn)
    duration = time.time() - start

    update_label(f"Prediction: {result}\nTime: {duration:.2f}s")

# ========================== TRAIN MODEL (VITModel.main()) ==========================
def train_model():
    update_label("Training started...")
    start = time.time()
    result = VITModel.main()
    duration = time.time() - start
    update_label(f"Training Completed!\n{result}\nTime: {duration:.2f}s")

# ========================== REAL-TIME DETECTION ==========================
def start_webcam():
    model = load_model("Insects_model.h5")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img = cv2.resize(frame, (64, 64))
        img = img.astype('float32') / 255.0
        img = np.expand_dims(img, axis=0)

        preds = model.predict(img)[0]
        idx = np.argmax(preds)
        label = f"{class_labels[idx]}: {preds[idx]*100:.2f}%"

        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow("Real-Time Insect Detection - Press 'q' to Exit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# ========================== EXIT APP ==========================
def window():
    root.destroy()

# ========================== BUTTONS ==========================
buttons = [
    ("📂 Browse Image", openimage),
    ("🧪 Preprocess Image", convert_grey),
    ("🤖 CNN Prediction", test_model),
    ("🎥 Real-Time Detection", start_webcam),
    ("🔧 Train Model", train_model),
    ("❌ Exit", window)
]

for i, (text, command) in enumerate(buttons):
    tk.Button(frame_controls, text=text, command=command, width=20, height=2,
              font=('Helvetica', 12, 'bold'), bg="white", fg="black").place(x=10, y=20 + i * 60)

root.mainloop()
