import tkinter as tk

def close_window(event):
    root.destroy()

def on_key_press(event):
    if event.char == 'p':
        close_window(event)

root = tk.Tk()

label = tk.Label(root, text="Premi il tasto 'p' dopo aver fatto 20 piegamenti")
label.pack()

root.bind('<Key>', on_key_press)
root.mainloop()
