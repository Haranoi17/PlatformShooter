from Scripts.Window import Window
from Scripts.Input import Input
from Scripts.Player import Player
from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
from Scripts.Platform import Platform
from Scripts.Bullet import Bullet
from Engine.FpsCounter import FpsCounter
from Engine.WorldEditor import WorldEditor

import pygame
import os
import random


class Engine:
    """Python predefined class functions"""
    def __init__(self):
        pygame.init()
        self.window = Window()
        self.player = Player()
        self.worldEditor = WorldEditor()
        self.frameRate = FpsCounter(1000)
        self.platforms = []
        self.gravity = 0.000006
        self.startTime = 0.0
        self.stopTime = pygame.time.get_ticks()
        self.deltaTime = self.stopTime - self.startTime
        self.lastClearTime = pygame.time.get_ticks()
        self._buildPlatforms()
        self.editWorld = False

    """Protected functions"""
    def _serveInput(self):
        Input.checkInputEvents()
        Input.updateMousePosition()

    def _calculateCollisions(self):
        Collidable.resetCollisions()
        Collidable.checkAllCollisions()

    def _updateLogic(self):
        self._calculateCollisions()

        for bullet in Bullet.bullets:
            bullet.update(self.deltaTime)

        self.player.update(self.deltaTime, self.gravity)

        self.window.update()

    def _draw(self):
        self.window.surface.fill((0, 0, 0))
        self.window.drawAnimated(self.player)
        self.window.drawHitBox(self.player)

        if self.editWorld:
            self.window.drawHitBox(self.worldEditor.mouseCollider)

        for bullet in Bullet.bullets:
            self.window.drawObject(bullet)
            self.window.drawHitBox(bullet)

        for platform in self.platforms:
            self.window.drawObject(platform)
            self.window.drawHitBox(platform)

        self.window.drawText(self.frameRate, Vector(40,40))

    def _deltaTime(self):
        self.deltaTime = self.stopTime - self.startTime

    def _buildPlatforms(self):
        for i in range(10):
            self.platforms.append(Platform(Vector(random.random() * 1000, random.random() * 500)))

    def _clearRoutine(self):
        """This method will clear unnecessary stuff like invisible bullets once in a while"""
        if pygame.time.get_ticks() - self.lastClearTime > 500:
            Bullet.removeOutOfBorder(self.window.getSize())
            self.lastClearTime = pygame.time.get_ticks()

    def _debugLog(self):
        print(self.player.flipped)
        pass

    def _wantToEditWorld(self):
        if Input.Num1 and not self.editWorld:
            self.editWorld = True
        if Input.Num2 and self.editWorld:
            self.editWorld = False

    """Public functions"""
    def runGame(self):
        while self.window.isOpen():
            self.startTime = pygame.time.get_ticks()

            self._debugLog()
            self._serveInput()

            self._wantToEditWorld()
            if self.editWorld:
                self.worldEditor.editWorld()
                self._calculateCollisions()
                self.window.update()
            else:
                self._updateLogic()

            self._draw()

            self._clearRoutine()
            self.frameRate.enable()

            self.stopTime = pygame.time.get_ticks()
            self._deltaTime()

