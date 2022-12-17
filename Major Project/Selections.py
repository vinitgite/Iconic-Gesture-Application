from tkinter import *
import subprocess

scr = Tk()
scr.title("Select Choice")
scr.geometry("500x200+470+200")

def PPT():
        scr.destroy()
        subprocess.call(["python","Instr_ppt.py"])

def Video():
        scr.destroy()
        subprocess.call(["python","Instr_Video.py"])

def Audio():
        scr.destroy()
        subprocess.call(["python", "Instr_Audio.py"])

def btn_ppt_on_enter(e):
   btn_ppt.config(background='OrangeRed3', foreground= "white")

def btn_ppt_on_leave(e):
   btn_ppt.config(background= 'SystemButtonFace', foreground= 'black')

def btn_video_on_enter(e):
   btn_video.config(background='OrangeRed3', foreground= "white")

def btn_video_on_leave(e):
   btn_video.config(background= 'SystemButtonFace', foreground= 'black')

def btn_audio_on_enter(e):
   btn_audio.config(background='OrangeRed3', foreground= "white")

def btn_audio_on_leave(e):
   btn_audio.config(background= 'SystemButtonFace', foreground= 'black')

lbl = Label(scr, text="Choose your Choice", font=("Cambria 18 bold"))
lbl.place(x=80,y=40)
btn_ppt= Button(scr, text="PPT", command=PPT, font=("Verdana 16 bold"), width=5, height=1)
btn_ppt.place(x=80, y=90)
btn_video = Button(scr, text="Video", command=Video, font=("Verdana 16 bold"), width=5, height=1)
btn_video.place(x=204, y=90)
btn_audio = Button(scr, text="Audio", command=Audio, font=("Verdana 16 bold"), width=5, height=1)
btn_audio.place(x=324, y=90)

btn_ppt.bind('<Enter>', btn_ppt_on_enter)
btn_ppt.bind('<Leave>', btn_ppt_on_leave)
btn_video.bind('<Enter>', btn_video_on_enter)
btn_video.bind('<Leave>', btn_video_on_leave)
btn_audio.bind('<Enter>', btn_audio_on_enter)
btn_audio.bind('<Leave>', btn_audio_on_leave)

scr.resizable(0,0)
scr.mainloop()
