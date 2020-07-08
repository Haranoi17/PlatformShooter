from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
import pygame
import os


class Entity:
    def __init__(self):
        self.healthPoints = 100
        self.speed = 0.5
        self.pos = Vector()
        self.imageOffset = Vector()
        self.width = 0
        self.height = 0
        self.image = None

    def move(self, deltaTime, moveDir):
        # Changes entities position
        self.pos = self.pos + moveDir * deltaTime * self.speed

    def update(self, deltaTime, gravity):
        pass

    def loadImage(self, path):
        self.image = pygame.image.load(path)
        self.width, self.height = self.image.get_size()

    def _calculateMoveDirection(self):
        # Returns normalized move direction vector
        pass

    def getDamage(self, amount):
        if self.healthPoints > 0:
            self.healthPoints -= amount
        else:
            pass
