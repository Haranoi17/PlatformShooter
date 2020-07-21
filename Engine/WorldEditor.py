from Engine.World import World
from Scripts.Platform import Platform
from Scripts.CollisionSystem import Collidable
from Scripts.Input import Input
from Scripts.Vector import Vector


class WorldEditor:
    # I dont understand why moving objects using mouseCollider does work only when this collider is static...
    # When I put it as a member variable it doesnt work... it works only on bullets which is impossibly weird since
    # all collidable derived are being saved in the same static array of collidable class. Why bullets have got extra
    # treatment?
    # mouseCollider = Collidable(Input.mousePos, Vector(2, 2))
    """Python predefined class functions"""
    def __init__(self):
        self.wantEditWorld = False


    """Static functions"""
    # @classmethod
    # def _updateMouseCollider(cls):
    #     cls.mouseCollider.updateCollidable(Input.mousePos)

    """Protected functions"""
    def _addPlatformAtPosition(self, pos):
        self.world.platforms.append(Platform(pos))

    def _moveObject(self, gameObject=Collidable()):
        gameObject.updateCollidable(Input.mousePos)

    """Public functions"""
    def editWorld(self):
        self._updateMouseCollider()
        if self.mouseCollider.other and Input.mouseLeft:
            self._moveObject(self.mouseCollider.other)
        if not self.mouseCollider.collided:
            self.other = None

    def wantToEditWorld(self):
        if Input.Num1 and not self.wantEditWorld:
            self.wantEditWorld = True
        if Input.Num2 and self.wantEditWorld:
            self.wantEditWorld = False





