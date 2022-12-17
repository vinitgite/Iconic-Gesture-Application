from tkinter import *
from tkinter.ttk import Progressbar
import sys
import cv2
from tkinter import messagebox
import subprocess

root = Tk()
root.resizable(0,0)

# Varibles
height = 150
width = 530
i=0

x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root.overrideredirect(1)

lbl_detect = Label(root, text="Detection of Camera", font=("yu gothic ui", 20, "bold"))
lbl_detect.place(x=140, y=10)

progress_lbl = Label(root, text='Please wait...',font=("yu gothic ui", 10, "bold"))
progress_lbl.place(x= 220, y=60)

progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=15, y=100)

def top():
    root.destroy()
    subprocess.call(["Python", "Selections.py"])


def load():
    global i, cap
    if i <= 10:
        txt = 'Please Wait... '+(str(10*i)+'%')
        progress_lbl.config(text=txt)
        progress_lbl.after(1000, load)
        progress['value'] = 10*i
        i += 1
        if cap is False:
            messagebox.showerror("Error", "Camera is not detected")
    else:
        messagebox.showinfo("Success", "Camera has been successfully detected !")
        top()

# Video Capture 
cap = cv2.VideoCapture(0)


load()
root.mainloop()