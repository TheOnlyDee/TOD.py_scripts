#learning python with GeeksForGeeks (geeksforgeeks.org)

import time

import tkinter

from tkinter import Tk

from tkinter import Button

root = Tk()

root.geometry('100x100')

btn = Button(root, text = "Click me!", bd = '5', command = root.destroy)

btn.pack(side = 'top')

root.mainloop()