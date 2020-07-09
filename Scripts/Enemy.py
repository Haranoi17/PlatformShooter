from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
from Scripts.Entity import Entity
from Scripts.CollisionSystem import Collidable


class Enemy(Entity, Collidable):
    """Python predefined class functions"""
    def __init__(self):
        Entity.__init__(self)
        Collidable.__init__(self)

    """Protected functions"""
    def _move(self, deltaTime, moveDir):
        """Changes entities position"""
        self.pos = self.pos + moveDir * deltaTime * self.speed

    def _calculateMoveDirection(self):
        """Returns normalized move direction vector"""
        pass

    """Public functions"""
    def update(self, deltaTime):
        pass

