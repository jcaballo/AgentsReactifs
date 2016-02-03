from random import *

from Content import Content
from Empty import Empty


class Agent(Content):
    def __init__(self, x, y, environment):
        super(Agent, self).__init__(x, y)
        self.environment = environment

    def next(self):
        randx = random.randint(-1, 1)
        randy = random.randint(-1, 1)
        if isinstance(self.environment[self.x + randx][self.y + randy], Empty):
            self.environment[self.x + randx][self.y + randy] = self
            self.environment[self.x][self.y] = Empty(self.x, self.y)
            self.x = self.x + randx
            self.y = self.y + randy

        elif isinstance(self.environment[self.x][self.y + randy], Empty):
            self.environment[self.x][self.y + randy] = self
            self.environment[self.x][self.y] = Empty(self.x, self.y)
            self.y = self.y + randy

        elif isinstance(self.environment[self.x + randx][self.y], Empty):
            self.environment[self.x + randx][self.y] = self
            self.environment[self.x][self.y] = Empty(self.x, self.y)
            self.x = self.x + randx
