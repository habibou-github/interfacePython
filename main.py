from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk

def showImage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="select Image",filetypes=(("ALL Files", "*.*"), ("JPG File", "*.jpg"), ("PNG File", "*.png")))
    img = Image.open(fln)
    img.thumbnail((350, 350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    lbl.place(x=50, y=50)

root = Tk()

lbl=Label(root)
lbl.pack()

browserButton = Button(root, text="Browser Image", padx=30, command=showImage)
browserButton.pack(side=tk.LEFT)
browserButton.place(x=100, y=450)

exitButton = Button(root, text="Exit", padx=30,  command=lambda: exit())
exitButton.pack()
exitButton.place(x=260, y=450)

runButton = Button(root, text="Segmenter", padx=30,  command=None)
runButton.pack()
runButton.place(x=600, y=450)



root.title("Segmentation des images")
root.geometry("900x500")
root.mainloop()