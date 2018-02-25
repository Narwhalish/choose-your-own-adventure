from Tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkFont

root = Tk()
root.title("Adventure in Time")
mainframe = Frame(root, padx=3, pady=12)
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)	

welcome_display_img = Image.open('welcome_display.jpg')
welcome_display = ImageTk.PhotoImage(welcome_display_img.resize((welcome_display_img.size[0]/3, welcome_display_img.size[1]/3), Image.BILINEAR))
welcome_title = "Adventure in Time"
welcome_font = Font(family=
welcome_screen = Label(mainframe, image=welcome_display, text=welcome_title, compound=CENTER)
welcome_screen.grid(column=1, row=1)

root.mainloop()