import random


class Food:
    def __init__(self):
        self.x = None
        self.y = None

    def randomize(self):
        self.x = random.randint(1,500)
        self.y = random.randint(1,500)
        return (self.x,self.y)
