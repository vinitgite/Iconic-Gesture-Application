from tkinter import *
from tkinter import Tk
from PIL import ImageTk
import subprocess


class instruction:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")
        self.root.geometry("1280x720+100+0")
        # ====== Bg Image ========
        self.bg = ImageTk.PhotoImage(file="background_image.jpg")
        Label(self.root, image=self.bg).place(relwidth=1, relheight=1)

        canvas = Canvas(self.root)
        canvas.create_image(0, 0, image=self.bg, anchor=NW)
        Button(text="PPT", font=('lato', 23, 'bold'), bd=0, cursor="hand2", bg="blue", width=7,
               command=self.btn_clicked_ppt).place(x=400, y=360)
        Button(text="VIDEO", font=('lato', 23, 'bold'), bd=0, cursor="hand2", bg="blue", width=7,
               command=self.btn_clicked_ppt_video).place(x=600, y=360)
        Button(text="AUDIO", font=('lato', 23, 'bold'), bd=0, cursor="hand2", bg="blue", width=7,
               command=self.btn_clicked_ppt_audio).place(x=800, y=360)

    def btn_clicked_ppt(self):
        # self.root.destroy()
        print("PPT")
    def btn_clicked_ppt_video(self):
        self.root.destroy()
        print("Video")
        # import select_vid
    
    def btn_clicked_ppt_audio(self):
        # self.root.destroy()
        print("Audio")

root = Tk()
obj = instruction(root)
root.mainloop()