from Scripts.Object import Object
from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
import pygame


class Platform(Object, Collidable):
    def __init__(self, pos):
        Object.__init__(self)
        self._loadImage("./resources/World/grass-platform.png")
        Collidable.__init__(self, box=Vector(self.width, self.height))

        self.updateCollidable(pos)

    def __str__(self):
        return "Platform"