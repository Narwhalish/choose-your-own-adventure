from Tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkFont
import webbrowser

def OpenURL(url):
    webbrowser.open_new(url)

root = Tk()
root.title('Adventure in Time')
mainframe = Frame(root, bg='DarkGoldenRod4')
mainframe.grid(column=0, row=0, sticky=N+E+S+W)

imgBG = Image.open('images/welcome_display.jpg')
welcome_display = ImageTk.PhotoImage(imgBG.resize((imgBG.size[0]/2, imgBG.size[1]/2), Image.BILINEAR))
welcome_font = tkFont.Font(family='Helvetica', size=36, weight='bold', underline=1)
welcome_screen = Label(mainframe, image=welcome_display, text='Adventure in Time', compound=CENTER, font=welcome_font, fg='white')
welcome_screen.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=N+E+S+W)

btnPlay = ttk.Button(mainframe, text='Play')
btnPlay.grid(column=0, row=1, columnspan=3, sticky=E+W, padx=5)


btnAbout = ttk.Button(mainframe, text='About')
btnAbout.grid(column=0, row=2, padx=5)

url="https://github.com/Narwhalish/choose-your-own-adventure"
btnSource = ttk.Button(mainframe, text='Source', command=lambda: OpenURL(url))
btnSource.grid(column=1, row=2, padx=5)

btnQuit = ttk.Button(mainframe, text='Quit', command=lambda: root.destroy())
btnQuit.grid(column=2, row=2, padx=5)

root.mainloop()