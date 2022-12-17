from tkinter import *
from tkinter import Tk
from PIL import ImageTk
import subprocess


class instruction:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")
        self.root.geometry("1160x610+160+70")
        # ====== Bg Image ========
        self.bg = ImageTk.PhotoImage(file="images/welcome.jpg")
        Label(self.root, image=self.bg).place(relwidth=1, relheight=1)

        canvas = Canvas(self.root)
        canvas.create_image(0, 0, image=self.bg, anchor=NW)
        Button(text="START", font=('lato', 18, 'bold'), bd=0, cursor="hand2", bg="white", width=9,
               command=self.btn_clicked).place(x=1010, y=550)

    def btn_clicked(self):
        self.root.destroy()
        import progress


root = Tk()
obj = instruction(root)
root.resizable(0, 0)
root.mainloop()
