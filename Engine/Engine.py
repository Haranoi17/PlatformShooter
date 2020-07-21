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
import threading
from ClientServer import Server

import pygame
import os
import random


class Engine:
    """Python predefined class functions"""

    def __init__(self, hasWindow=True):
        pygame.init()
        self.hasWindow = hasWindow
        if self.hasWindow:
            self.window = Window()
        self.world = World()
        self.worldEditor = WorldEditor()
        self.frameRate = FpsCounter(1000)
        self.gravity = 0.000000000000000006
        self.startTime = 0.0
        self.player = Player(1)
        self.stopTime = pygame.time.get_ticks()
        self.deltaTime = self.stopTime - self.startTime
        self.lastClearTime = pygame.time.get_ticks()
        self.editWorld = False
        self.drawHitbox = True

    """Protected functions"""

    def _calculateCollisions(self):
        Collidable.resetCollisions()
        Collidable.checkAllCollisions()
        print(self.player.collisionInfo)

    def _updateLogic(self):
        Input.updateMousePosition()
        Input.checkInputEvents()
        self._calculateCollisions()

        for bullet in Bullet.bullets:
            bullet.update(self.deltaTime)

        for platform in self.world.platforms:
            platform.updateCollidable(platform.pos)

        for player in self.world.players:
            player.update(self.deltaTime, self.gravity)

        self.player.update(self.deltaTime, self.gravity)
        if self.hasWindow:
            self.window.update()

    def _draw(self):
        self.window.surface.fill((0, 0, 0))
        for player in self.world.players:
            self.window.drawAnimated(player)
            if self.drawHitbox:
                self.window.drawHitBox(player)


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

        self.window.drawAnimated(self.player)
        self.window.drawHitBox(self.player)
        self.window.drawText(self.frameRate, Vector(40, 40))

    def _deltaTime(self):
        self.deltaTime = self.stopTime - self.startTime

    def _clearRoutine(self):
        """This method will clear unnecessary stuff like invisible bullets once in a while"""
        if pygame.time.get_ticks() - self.lastClearTime > 500:
            Bullet.removeOutOfBorder(Vector(1920, 1080))
            self.lastClearTime = pygame.time.get_ticks()

    def _debugLog(self):
        pass

    """Public functions"""

    def movePlayer(self, ID=str, moveDir=Vector):
        for player in self.world.players:
            if str(player.ID) == ID:
                player.moveDir = moveDir

    def registerPlayer(self, ID):
        self.world.players.append(Player(ID))

    def updateServer(self):
        self.startTime = pygame.time.get_ticks()
        self._updateLogic()

        self._draw()

        self.frameRate.enable()
        self._clearRoutine()
        self.stopTime = pygame.time.get_ticks()
        self._deltaTime()

    def updateClient(self):
        self._updateLogic()
        self._draw()
        self.window.update()
        self.frameRate.enable()

    def runGame(self):
        while self.window.isOpen():
            self.startTime = pygame.time.get_ticks()

            self._debugLog()

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
