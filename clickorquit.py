#learning python with GeeksForGeeks (geeksforgeeks.org)

from tkinter import *

from tkinter.ttk import *

root = Tk()

root.geometry('150x150')

style = Style()

style.configure('TButton', font =('calibri', 10, 'bold', 'underline'), foreground = 'red')

btn1 = Button(root, text = 'Quit !', style = 'TButton', command = root.destroy)

btn1.grid(row = 0, column = 3, padx = 100)

btn2 = Button(root, text = "Click Me!", command = None)

btn2.grid(row = 1, column = 3, pady = 10, padx = 100) 

root.mainloop()