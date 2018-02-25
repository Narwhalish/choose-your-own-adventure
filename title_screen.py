from Tkinter import *
from tkinter import ttk

root = Tk()
root.title("Adventure in Time")
mainframe = Frame(root, padx=3, pady=12)
mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)	

welcome_display = BitmapImage('welcome_screen.XBM')
welcome_title = "Adventure in Time"
welcome_screen = Label(mainframe, image=welcome_display, text=welcome_title)
welcome_screen.grid()

root.mainloop()