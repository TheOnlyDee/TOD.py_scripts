#learning python with GeeksForGeeks (geeksforgeeks.org)

from tkinter import * 
from tkinter.ttk import *
  
root = Tk()
  
# Adding widgets to the root window
Label(root, text = 'Tod (just geeks for geeks copy-pasted)', font =(
  'Calibri', 15)).pack(side = TOP, pady = 10)
  
# Creating a photoimage object to use image
photo = PhotoImage(file = r"/home/paorrot/Downloads/circle.png")
  
# here, image option is used to
# set image on button
Button(root, text = 'Click Me !', image = photo).pack(side = TOP)
  
mainloop()