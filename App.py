import pygame as pygame
from Snake import Player
class App:
    def __init__(self):
        #Clock sets frame rate
        self.__clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_mode((300, 300), pygame.HWSURFACE)
        self.__Snake = Player()

    def setfps(self):
        self.__clock.tick(60)

    def checkinput(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    print("Down was pressed")
                    self.__Snake.movedown()
                elif event.key == pygame.K_UP:
                    print('Up was pressed')
                    self.__Snake.moveup()
                elif event.key == pygame.K_RIGHT:
                    print('Right was pressed')
                    self.__Snake.moveright()
                elif event.key == pygame.K_LEFT:
                    print('Left was pressed')
                    self.__Snake.moveleft()
                #Terminating key
                elif event.key == pygame.K_q:
                    print("Exiting")
                    pygame.quit()
                    exit()

if __name__ == '__main__':
    testapp = App()
    testapp.setfps()
    while True:
        testapp.checkinput()
