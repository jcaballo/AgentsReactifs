from random import *
from tkinter import *

from Content import Content
from Empty import Empty



class Agent(Content):
    def __init__(self, x, y, environment):
        super(Agent, self).__init__(x, y, environment.fenetre)
        self.environment = environment

    def next(self):
        randx = randint(-1, 1)
        randy = randint(-1, 1)
        if self.x + randx >= 0 \
                and self.x + randx < self.environment.i \
                and self.y + randy >= 0 \
                and self.y + randy < self.environment.j \
                and isinstance(self.environment.matrice[self.x + randx][self.y + randy], Empty):
            self.environment.matrice[self.x + randx][self.y + randy] = self
            self.environment.matrice[self.x][self.y] = Empty(self.x, self.y, self.fenetre)
            self.x = self.x + randx
            self.y = self.y + randy

        elif self.y + randy >= 0 \
                and self.y + randy < self.environment.j \
                and isinstance(self.environment.matrice[self.x][self.y + randy], Empty):
            self.environment.matrice[self.x][self.y + randy] = self
            self.environment.matrice[self.x][self.y] = Empty(self.x, self.y, self.fenetre)
            self.y = self.y + randy

        elif self.x + randx >= 0 \
                and self.x + randx < self.environment.i \
                and isinstance(self.environment.matrice[self.x + randx][self.y], Empty):
            self.environment.matrice[self.x + randx][self.y] = self
            self.environment.matrice[self.x][self.y] = Empty(self.x, self.y, self.fenetre)
            self.x = self.x + randx

        self.label = Label(self.fenetre, text="%s" % "    ", bg="red")
        self.label.grid(row=self.x, column=self.y, padx=(1, 1), pady=(1, 1))
