class Player:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.direction = "DOWN"
        self.body = [(self.x,self.y)]

    def moveleft(self):
        self.x -= 1

    def moveright(self):
        self.x += 1

    def moveup(self):
        self.y -= 1

    def movedown(self):
        self.y += 1

    def move(self):
        if self.direction == "DOWN":
            self.movedown()
        elif self.direction == "UP":
            self.moveup()
        elif self.direction == "LEFT":
            self.moveleft()
        elif self.direction == "RIGHT":
            self.moveright()

    def checkeat(self, food):
        if (food.x, food.y) == (self.x, self.y):
            return True
        else:
            return False
