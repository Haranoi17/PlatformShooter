from Scripts.Window import Window
from Scripts.Input import Input
from Scripts.Player import Player
from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
from Scripts.Platform import Platform
from Scripts.Bullet import Bullet
from Engine.FpsCounter import FpsCounter
from Engine.WorldEditor import WorldEditor
from Engine.World import World

import pygame
import os
import random


class Engine:
    """Python predefined class functions"""

    def __init__(self):
        pygame.init()
        self.window = Window()
        self.world = World()
        self.worldEditor = WorldEditor()
        self.frameRate = FpsCounter(1000)
        self.gravity = 0.000006
        self.startTime = 0.0
        self.stopTime = pygame.time.get_ticks()
        self.deltaTime = self.stopTime - self.startTime
        self.lastClearTime = pygame.time.get_ticks()
        self.editWorld = False
        self.drawHitbox = True

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

        self.world.player.update(self.deltaTime, self.gravity)
        self.window.update()

    def _draw(self):
        self.window.surface.fill((0, 0, 0))
        self.window.drawAnimated(self.world.player)
        if self.drawHitbox:
            self.window.drawHitBox(self.world.player)

        if self.editWorld and self.drawHitbox:
            self.window.drawHitBox(self.worldEditor.mouseCollider)

        for bullet in Bullet.bullets:
            self.window.drawObject(bullet)
            if self.drawHitbox:
                self.window.drawHitBox(bullet)

        for platform in self.world.platforms:
            self.window.drawObject(platform)
            if self.drawHitbox:
                self.window.drawHitBox(platform)

        self.window.drawText(self.frameRate, Vector(40, 40))

    def _deltaTime(self):
        self.deltaTime = self.stopTime - self.startTime

    def _clearRoutine(self):
        """This method will clear unnecessary stuff like invisible bullets once in a while"""
        if pygame.time.get_ticks() - self.lastClearTime > 500:
            Bullet.removeOutOfBorder(self.window.getSize())
            self.lastClearTime = pygame.time.get_ticks()

    def _debugLog(self):
        pass

    """Public functions"""

    def runGame(self):
        while self.window.isOpen():
            self.startTime = pygame.time.get_ticks()

            self._debugLog()
            self._serveInput()

            self.worldEditor.wantToEditWorld()
            if self.worldEditor.wantEditWorld:
                if Input.mouseLeft and Input.mouseRight:
                    self.world.saveWorld()
                if Input.mouseLeft and Input.down and Input.up:
                    self.world.loadWorld()
                self._calculateCollisions()
                self.worldEditor.editWorld()

                self.window.update()
            else:
                self._updateLogic()

            self._draw()

            self._clearRoutine()
            self.frameRate.enable()

            self.stopTime = pygame.time.get_ticks()

            self._deltaTime()
