from Scripts.Object import Object
from Scripts.CollisionSystem import Collidable
from Scripts.Vector import Vector
from Scripts.Bullet import Bullet

import pygame


class Gun(Object, Collidable):
    """Python predefined class functions"""
    def __init__(self):
        self.shootDelay = 200  # ms
        self.lastShootTime = 0

    """Public functions"""
    def shoot(self, pos, immunePlayer, relativeMousePos=Vector()):
        """Gun creates bullet object which stores itself in Bullets' class static array"""
        if pygame.time.get_ticks() - self.lastShootTime > self.shootDelay:
            Bullet(relativeMousePos, immunePlayer, pos)
            self.lastShootTime = pygame.time.get_ticks()
