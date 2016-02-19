from random import *
from tkinter import *

from Agent import Agent
from Empty import Empty
from PheromoneExploration import PheromoneExploration
from PheromoneTauxZero import PheromoneTauxZero


class Explorateur(Agent):
    visite = []

    def __init__(self, x, y, environment):
        super(Explorateur, self).__init__(x, y, environment)
        self.label.config(bg="red")

    def next(self):
        randx = randint(-1, 1)
        randy = randint(-1, 1)
        self.environment.pheromones[self.x][self.y] = PheromoneExploration(10)
        if self.x + randx >= 0 \
                and self.x + randx < self.environment.i \
                and self.y + randy >= 0 \
                and self.y + randy < self.environment.j \
                and isinstance(self.environment.matrice[self.x + randx][self.y + randy], Empty) \
                and (isinstance(self.environment.pheromones[self.x + randx][self.y + randy],
                                PheromoneTauxZero) or self.estBloque()):
            self.environment.matrice[self.x + randx][self.y + randy] = self
            self.environment.matrice[self.x][self.y] = Empty(self.x, self.y, self.fenetre)
            self.x = self.x + randx
            self.y = self.y + randy

        elif self.y + randy >= 0 \
                and self.y + randy < self.environment.j \
                and isinstance(self.environment.matrice[self.x][self.y + randy], Empty) \
                and (isinstance(self.environment.pheromones[self.x][self.y + randy],
                                PheromoneTauxZero) or self.estBloque()):
            self.environment.matrice[self.x][self.y + randy] = self
            self.environment.matrice[self.x][self.y] = Empty(self.x, self.y, self.fenetre)
            self.y = self.y + randy

        elif self.x + randx >= 0 \
                and self.x + randx < self.environment.i \
                and isinstance(self.environment.matrice[self.x + randx][self.y], Empty) \
                and (isinstance(self.environment.pheromones[self.x + randx][self.y],
                                PheromoneTauxZero) or self.estBloque()):
            self.environment.matrice[self.x + randx][self.y] = self
            self.environment.matrice[self.x][self.y] = Empty(self.x, self.y, self.fenetre)
            self.x = self.x + randx

        self.label = Label(self.fenetre, text="%s" % "    ", bg="red")
        self.label.grid(row=self.x, column=self.y, padx=(1, 1), pady=(1, 1))

    def estBloque(self):
        if self.x - 1 >= 0 and self.y - 1 > 0 and not isinstance(self.environment.pheromones[self.x - 1][self.y - 1],
                                                                 PheromoneTauxZero) \
                and self.x - 1 >= 0 and not isinstance(self.environment.pheromones[self.x - 1][self.y],
                                                       PheromoneTauxZero) \
                and self.x - 1 >= 0 and self.y + 1 < self.environment.j and not isinstance(
            self.environment.pheromones[self.x - 1][self.y + 1], PheromoneTauxZero) \
                and self.y - 1 >= 0 and not isinstance(self.environment.pheromones[self.x][self.y - 1],
                                                       PheromoneTauxZero) \
                and self.y + 1 < self.environment.j and not isinstance(self.environment.pheromones[self.x][self.y + 1],
                                                                       PheromoneTauxZero) \
                and self.x + 1 < self.environment.i and self.y - 1 >= 0 and not isinstance(
            self.environment.pheromones[self.x + 1][self.y - 1], PheromoneTauxZero) \
                and self.x + 1 < self.environment.i and not isinstance(self.environment.pheromones[self.x + 1][self.y],
                                                                       PheromoneTauxZero) \
                and self.x + 1 < self.environment.i and self.y + 1 < self.environment.j and not isinstance(
            self.environment.pheromones[self.x + 1][self.y + 1], PheromoneTauxZero):
            return True

        return False
