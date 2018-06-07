import pygame as pygame
from Food import Food
from Snake import Player
import time
SIZE = 13


class App:
    def __init__(self):
        self.__Snake = Player()
        self.__Food = Food()
        self.__Display = None

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        self.setfps(clock,60)
        self.setupdisplay()

        while True:

            self.insertsquare()
            self.checkinput()
            self.__Snake.move()
            self.__Display.fill((0, 0, 0))
            time.sleep(3.0 / 1000.0);

    def insertsquare(self):
        if(self.__Snake.checkeat(self.__Food)):
            pygame.draw.rect(self.__Display, (25, 200, 150), pygame.Rect(self.__Food.randomize(), (SIZE, SIZE)))
        else:
            pygame.draw.rect(self.__Display, (25, 200, 150), pygame.Rect((self.__Food.x, self.__Food.y), (SIZE, SIZE)))
        pygame.draw.rect(self.__Display, (100, 200, 0), pygame.Rect((self.__Snake.x, self.__Snake.y), (SIZE, SIZE)))
        pygame.display.update()

    def setupdisplay(self):
        self.__Display = pygame.display.set_mode((500, 500), 0, 32)
        pygame.display.set_caption('Snake Game')
        pygame.draw.rect(self.__Display, (100, 200, 0), pygame.Rect((self.__Snake.x, self.__Snake.y), (SIZE, SIZE)))
        pygame.draw.rect(self.__Display, (25, 200, 150), pygame.Rect((self.__Food.randomize()), (SIZE, SIZE)))
        pygame.display.update()

    def setfps(self, clock, fps):
        clock.tick(fps)

    def checkinput(self):
        for event in pygame.event.get():
            self.processevent(event)

    def processevent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("Down was pressed")
                self.__Snake.direction = "DOWN"
            elif event.key == pygame.K_UP:
                print('Up was pressed')
                self.__Snake.direction = "UP"
            elif event.key == pygame.K_RIGHT:
                print('Right was pressed')
                self.__Snake.direction = "RIGHT"
            elif event.key == pygame.K_LEFT:
                print('Left was pressed')
                self.__Snake.direction = "LEFT"
            #               Terminating key
            elif event.key == pygame.K_q:
                print("Exiting")
                pygame.quit()
                exit()


if __name__ == '__main__':
    testapp = App()
    testapp.run()

