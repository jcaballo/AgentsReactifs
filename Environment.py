from random import *
from tkinter import *

from Empty import Empty
from PheromoneStation import PheromoneStation
from PheromoneTauxZero import PheromoneTauxZero
from Station import Station
from Worth import Worth
from Worthless import Worthless


class Environment: # Définition de notre classe Personne

    matrice = []
    pheromones = []
    agents = []
    nbWorth = 5
    nbWorthless = 5

    def __init__(self, _i, _j):
        self.fenetre = Tk()
        self.i = _i
        self.j = _j
        for i in range(0, _i):
            self.matrice.append([])
            self.pheromones.append([])
            for j in range(0, _j):
                if (i == _i - 1 and j == _j - 1):
                    station = Station(i, j, self)
                    self.matrice[i].append(station)
                    self.agents.append(station)
                    self.pheromones[i].append(PheromoneStation())

                else:
                    des = randint(1, 200)
                    if (des <= 2 and self.nbWorth != 0):
                        self.matrice[i].append(Worth(i, j, self.fenetre))
                        self.nbWorth -= 1
                    elif (des <= 4 and self.nbWorthless != 0):
                        self.matrice[i].append(Worthless(i, j, self.fenetre))
                        self.nbWorthless -= 1
                    else:
                        self.matrice[i].append(Empty(i, j, self.fenetre))
                    self.pheromones[i].append(PheromoneTauxZero())

        self.fenetre.after(500, self.advance)
        self.fenetre.mainloop()

    def advance(self):
        for agent in self.agents:
            agent.next()
        for pheromoneX in self.pheromones:
            for pheromoneY in pheromoneX:
                pheromoneY.next()
        self.fenetre.update_idletasks()
        self.fenetre.after(500, self.advance)
