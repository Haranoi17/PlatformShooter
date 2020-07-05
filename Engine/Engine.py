from Scripts.Window import Window
from Scripts.Input import Input
from Scripts.Player import Player
from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
from Scripts.Platform import Platform

import pygame
import os
import random



class Engine:
    def __init__(self):
        pygame.init()
        self.window = Window()
        self.player = Player()
        self.platforms = []
        self.gravity = 0.000002
        self.startTime = 0.0
        self.stopTime = pygame.time.get_ticks()
        self.deltaTime = self.stopTime - self.startTime
        self.buildPlatforms()

    def runGame(self):
        while self.window.isOpen():
            self.startTime = pygame.time.get_ticks()

            self.debugLog()
            self._serveInput()
            self._updateLogic()
            self._draw()

            self.stopTime = pygame.time.get_ticks()
            self._deltaTime()

    def _serveInput(self):
        Input.checkInputEvents()

    def _updateLogic(self):
        Collidable.resetCollisions()
        Collidable.checkAllCollisions()
        self.player.update(self.deltaTime, self.gravity)
        self.window.update()

    def _draw(self):
        self.window.surface.fill((0, 0, 0))
        self.window.drawEntity(self.player)
        self.window.drawHitBox(self.player)

        for platform in self.platforms:
            self.window.drawObject(platform)

    def _deltaTime(self):
        self.deltaTime = self.stopTime - self.startTime

    def buildPlatforms(self):
        for i in range(10):
            self.platforms.append(Platform(Vector(random.random()*1000, random.random()*500)))

    def debugLog(self):
        print(f"{self.player.collisionInfo} {self.player.jumpTime}")