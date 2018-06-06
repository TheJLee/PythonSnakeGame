import pygame as pygame


class Player:
    def __init__(self):
        self.__x = 10
        self.__y = 10
    def moveLeft(self):
        self.__x -= 1

    def moveRight(self):
        self.__x += 1

    def moveUp(self):
        self.__y += 1

    def moveDown(self):
        self.__y -= 1

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_mode((300, 300), pygame.HWSURFACE)


    while True:
        pygame.event.pump()
        state = pygame.key.get_pressed()

        for down in state:
            if down:
                print(down)
        pygame.event.pump()
