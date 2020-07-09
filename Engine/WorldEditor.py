from Engine.World import World
from Scripts.Platform import Platform
from Scripts.CollisionSystem import Collidable
from Scripts.Input import Input
from Scripts.Vector import Vector


class WorldEditor:
    """Python predefined class functions"""
    def __init__(self, world=World()):
        self.world = world
        self.mouseCollider = Collidable(Input.mousePos, Vector(1, 1))

    """Protected functions"""
    def _addPlatformAtPosition(self, pos):
        self.world.platforms.append(Platform(pos))

    def _moveObject(self, gameObject=Collidable()):
        gameObject.updateCollidable(Input.mousePos)

    def _updateMouseCollider(self):
        self.mouseCollider.updateCollidable(Input.mousePos)

    """Public functions"""
    def editWorld(self):
        self._updateMouseCollider()
        if self.mouseCollider.otherReference and Input.mouseLeft:
            self._moveObject(self.mouseCollider.otherReference)





