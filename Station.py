from Agent import Agent
from Empty import Empty
from Explorateur import Explorateur


class Station(Agent):
    nbExplorateur = 5

    def __init__(self, x, y, environment):
        super(Station, self).__init__(x, y, environment)
        self.label.config(bg="yellow")

    def next(self):
        if (isinstance(self.environment.matrice[self.environment.i - 2][self.environment.j - 1],
                       Empty) and self.nbExplorateur > 0):
            explorateur = Explorateur(self.environment.i - 2, self.environment.j - 1, self.environment)
            self.environment.matrice[self.environment.i - 2][self.environment.j - 1] = explorateur
            self.environment.agents.append(explorateur)
            self.nbExplorateur -= 1
