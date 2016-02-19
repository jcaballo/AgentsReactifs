from tkinter import *

class Content():
    def __init__(self, x, y, fenetre):
        self.x = x
        self.y = y
        self.fenetre = fenetre
        self.label = Label(fenetre, text="%s" % "    ", bg="lightgrey" )
        self.label.grid(row=self.x, column=self.y, padx=(1,1) ,pady=(1,1))
