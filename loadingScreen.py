from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

root = Tk()
image = PhotoImage(file="images/loading_screen.png")

height = 430
width = 530

x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(True)

root.config(background="#0f172a")

bg_label = Label(root, image=image, bg="#0f172a")
bg_label.place(relx = 0.5, rely = 0.5, anchor=CENTER)

progress_label = Label(root, text="Loading . . . ", font=("Trebuchet Ms", 12, "bold"), fg="white", bg="#0f172a")
progress_label.place(relx = 0.5, rely = 0.83, anchor = CENTER)

progress = ttk.Style()
progress.theme_use('clam')
progress.configure("red.Horizontal.TProgressbar", background="#108cff")

progress = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate',
                       style='red.Horizontal.TProgressbar')
progress.place(relx = 0.12, y = 375)

def top():
    root.withdraw()
    os.system("python dashboard.py")
    root.destroy()

i = 0

def load():
    global i

    if i <= 10:
        txt = 'Loading . . .' + (str(10*i) + '%')
        progress_label.config(text=txt)
        progress_label.after(300, load)
        progress['value'] = 10*i
        i += 1
    else:
        top()

load()
root.resizable(False, False)
root.mainloop()