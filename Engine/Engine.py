from Scripts.Window import Window
from Scripts.Input import Input
from Scripts.Player import Player
from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable

import pygame
import os

class Engine:
    def __init__(self):
        pygame.init()
        self.window = Window()
        # Window.surface.blit(bg, (0,0))
        self.player = Player()
        self.deltaTime = pygame.time.get_ticks()
        # clock.tick(27) #27 klatek na sekunde
        self.img = pygame.image.load(os.path.join("./resources", "character.png"))

    def runGame(self):
        while self.window.isOpen():
            self.deltaTime = pygame.time.get_ticks() - self.deltaTime
            self._serveInput()
            self._updateLogic()
            self._draw()

    def _serveInput(self):
        Input.checkInputEvents()

    def _updateLogic(self):
        self.player.update(self.deltaTime)
        Collidable.checkAllCollisios()
        self.window.update()
        Collidable.resetCollisions()

    def _draw(self):
        self.window.draw(self.img, self.player.pos)
        # self.window.draw(char, collid.pos)
