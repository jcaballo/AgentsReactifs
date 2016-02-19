from random import *


class Pheromone:
    def __init__(self, taux):
        self.taux = taux

    def next(self):
        if (self.taux > 0):
            des = randint(0, 1)
            self.taux -= 0.1
