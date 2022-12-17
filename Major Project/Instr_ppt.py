from tkinter import *
from PIL import ImageTk, Image
import subprocess

myScr = Tk()
myScr.geometry("1290x760+120+10")

def selection():
   myScr.destroy()
   subprocess.call(["python","selection_of_ppt.py"])

def back(): 
    myScr.destroy()
    subprocess.call(["python","Selections.py"])

def btn_video_on_enter(e):
   btn_next.config(background='Red3', foreground= "white")

def btn_video_on_leave(e):
   btn_next.config(background= 'SystemButtonFace', foreground= 'black')
def btn_back_on_enter(e):
   btn_back.config(background='Black', foreground= "white")

def btn_back_on_leave(e):
   btn_back.config(background= 'SystemButtonFace', foreground= 'black')

# --------------- Background Image --------------------
bg = ImageTk.PhotoImage(file="images/background_ppt.jpg")
Label(myScr, image=bg).place(relwidth=1, relheight=1)


btn_next = Button(myScr, text='Next', font=('lato 20 bold'), width=7, height=1, command=selection)
btn_next.place(x=1150, y=695)
btn_back = Button(myScr, text='Back', font=('lato 20 bold'), width=7, height=1, command=back)
btn_back.place(x=20, y=695)
btn_next.bind('<Enter>', btn_video_on_enter)
btn_next.bind('<Leave>', btn_video_on_leave)
btn_back.bind('<Enter>', btn_back_on_enter)
btn_back.bind('<Leave>', btn_back_on_leave)

myScr.resizable(0,0)
myScr.mainloop()

#.geometry("1290x760+120+10")