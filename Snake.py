import pygame as pygame

class Player:
    def __init__(self):
        self.__x = 10
        self.__y = 10

    def moveleft(self):
        self.__x -= 1

    def moveright(self):
        self.__x += 1

    def moveup(self):
        self.__y += 1

    def movedown(self):
        self.__y -= 1
