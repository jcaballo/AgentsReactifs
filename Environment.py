from Agent import Agent
from Empty import Empty
from tkinter import *
from time import sleep

class Environment: # Définition de notre classe Personne

    matrice = []
    agents = []

    def __init__(self, _i, _j):
        self.fenetre = Tk()
        self.i = _i
        self.j = _j
        for i in range(0, _i):
            self.matrice.append([])
            for j in range(0, _j):
                if i == 0 and j == 0:
                    agent = Agent(i, j, self)
                    self.matrice[i].append(agent)
                    self.agents.append(agent)
                else:
                    self.matrice[i].append(Empty(i, j,  self.fenetre))
        self.fenetre.after(2000, self.advance)
        self.fenetre.mainloop()

    def advance(self):
         for agent in self.agents:
            agent.next();
            self.fenetre.update_idletasks()
            self.fenetre.after(2000, self.advance)





