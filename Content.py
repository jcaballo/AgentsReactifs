from tkinter import *

class Content():
    def __init__(self, x, y, fenetre):
        self.x = x
        self.y = y
        self.fenetre = fenetre
        self.label = Label(fenetre, text="%s" % (type(self)), bg="lightgrey" )
        self.label.grid(row=self.x, column=self.y, padx=(10,10) ,pady=(10,10))
