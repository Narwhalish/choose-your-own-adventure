from Tkinter import *

class Room(Frame):
    def __init__(self, parent, dimensions, objects):
        Frame.__init__(self, parent)
        self.parent = parent
        