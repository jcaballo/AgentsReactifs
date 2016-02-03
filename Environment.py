from Agent import Agent
from Empty import Empty

class Environment: # Définition de notre classe Personne

    matrice = []
    def __init__(self, _i, _j):
        for i in range(0, _i):
            self.matrice.append([])
            for j in range(0, _j):
                if i == 0 & j == 0:
                    self.matrice[i].append(Agent(i, j, self))
                else:
                    self.matrice[i].append(Empty(i, j))
