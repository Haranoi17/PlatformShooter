from Scripts.Window import Window
from Scripts.Input import Input
from Scripts.Player import Player
from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
from Scripts.Platform import Platform

import pygame
import os


class Engine:
    def __init__(self):
        pygame.init()
        self.window = Window()
        self.player = Player()
        self.platform = Platform(Vector(800,300))
        self.startTime = 0.0
        self.stopTime = pygame.time.get_ticks()
        self.deltaTime = self.stopTime - self.startTime

    def runGame(self):
        while self.window.isOpen():
            self.startTime = pygame.time.get_ticks()

            self._serveInput()
            self._updateLogic()
            self._draw()
            print(f"{self.player.collisionInfo}")

            self.stopTime = pygame.time.get_ticks()
            self._deltaTime()

    def _serveInput(self):
        Input.checkInputEvents()

    def _updateLogic(self):
        Collidable.resetCollisions()
        Collidable.checkAllCollisions()
        self.player.update(self.deltaTime)
        self.platform.update()
        self.window.update()

    def _draw(self):
        self.window.surface.fill((0, 0, 0))
        self.window.drawEntity(self.player)
        self.window.drawObject(self.platform)
        self.window.drawHitBox(self.player)
        self.window.drawHitBox(self.platform)

    def _deltaTime(self):
        self.deltaTime = self.stopTime - self.startTime
