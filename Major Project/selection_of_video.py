from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import subprocess

def browse():
    global filename
    filename = fd.askopenfilename(title='Choose video file ', initialdir=r'C:\Users\varun\Videos',filetypes=[('Video files',['*.mp4','*.mkv'])])
    entPath.insert(0, filename) # Fill the entry with filename

def play():
    if entPath.get() == "":
        messagebox.showwarning('Warning', 'Please select file')
    else:
        os.startfile(entPath.get())
        myScr.destroy()
        subprocess.call(["python", "media.py"])

def Instruction():
    myScr.destroy()
    subprocess.call(["python", "Instr_Video.py"])

#define main wondow
myScr = Tk()
myScr.title("File selecting window")
myScr.geometry('600x140+300+70')
varPath = StringVar
myScr.resizable(0,0)
# Lable
lblPath = Label(myScr, text="Choose video file")
lblPath.grid(row=1, column=0, padx=10, pady=20)

# Entry
entPath = Entry(myScr, textvariable=varPath, width=65)
entPath.grid(row=1, column=1)

# Buttons
btnBrowse = Button(myScr, text="Choose", command=browse)
btnBrowse.grid(row=1, column=2, padx=10)
btnNext = Button(myScr, text="Next", command=play)
btnNext.grid(row=2, column=1, padx=10)
btn_back = Button(myScr, text="Instruction", width=9, height=1, command=Instruction)
btn_back.grid(row=3, column=1, padx=20, pady=10)
myScr.mainloop()