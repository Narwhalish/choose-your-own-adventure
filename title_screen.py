from Tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkFont, webbrowser, os
import main
"""
Name: Emily Liu, Bryan Yao, Karena Yan 
Course: CSE 
Assignment: Choose your Own Adventure
Description: Billy Pilgrim -- Lost in Time

Creates interactive title screen with Tk elements and PIL objects.
"""

"""Opens a given URL with using the webbrowser module
Args:
    URL (str)
Returns:
    N/A
"""
def OpenURL(url):
    webbrowser.open_new(url)
    
def SwitchFrames(new, old):
    new.grid(row=0, column=0, sticky=N+E+S+W)
    old.grid_remove()

"""Initialize main root window of title screen."""
root = Tk()
root.title('Adventure in Time')

"""Create screen frames"""
mainframe = Frame(root, bg='DarkGoldenRod4')
mainframe.grid(column=0, row=0, sticky=N+E+S+W)
dialogueframe = Frame(root)

"""Read image data from stored background image and compound it with a label."""
mainframe_imgBG = Image.open('images/welcome_display.jpg')
welcome_display = ImageTk.PhotoImage(mainframe_imgBG)
welcome_font = tkFont.Font(family='Helvetica', size=42, weight='bold', underline=1)
welcome_screen = Label(mainframe, image=welcome_display, text='Adventure in Time', compound=CENTER, font=welcome_font, fg='white')
welcome_screen.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=N+E+S+W)

"""Create Play button with callback to main.py"""
mainframe_btnPlay = ttk.Button(mainframe, text='Play', command=lambda: SwitchFrames(dialogueframe, mainframe))
mainframe_btnPlay.grid(column=0, row=1, columnspan=3, sticky=E+W, padx=30)

"""Create About button with callback to README.md"""
mainframe_btnAbout = ttk.Button(mainframe, text='About')
mainframe_btnAbout.grid(column=0, row=2, padx=5, pady=5)

"""Create Source button with callback to OpenURL to open source code on GitHub"""
source_url="https://github.com/Narwhalish/choose-your-own-adventure"
mainframe_btnSource = ttk.Button(mainframe, text='Source', command=lambda: OpenURL(source_url))
mainframe_btnSource.grid(column=1, row=2, padx=5, pady=5)

"""Create Quit button to destroy root window and widgets."""
mainframe_btnQuit = ttk.Button(mainframe, text='Quit', command=lambda: root.destroy())
mainframe_btnQuit.grid(column=2, row=2, padx=5, pady=5)

dialogueframe_lblNarrativeVar = StringVar()
dialogueframe_lblNarrative = Label(dialogueframe, relief=RIDGE, textvariable=dialogueframe_lblNarrativeVar)
dialogueframe_lblNarrative.grid(column=0, row=0, padx=5, pady=5)

"""Start mainloop"""
root.mainloop()