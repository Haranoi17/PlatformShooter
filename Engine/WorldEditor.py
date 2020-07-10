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
    mouseCollider = Collidable(Input.mousePos, Vector(2, 2))
    """Python predefined class functions"""
    # none

    """Static functions"""
    @classmethod
    def _updateMouseCollider(cls):
        cls.mouseCollider.updateCollidable(Input.mousePos)

    """Protected functions"""
    def _addPlatformAtPosition(self, pos):
        self.world.platforms.append(Platform(pos))

    def _moveObject(self, gameObject=Collidable()):
        gameObject.updateCollidable(Input.mousePos)



    """Public functions"""
    def editWorld(self):
        self._updateMouseCollider()
        #print(self.mouseCollider.otherReference)
        if self.mouseCollider.otherReference and Input.mouseLeft:
            self._moveObject(self.mouseCollider.otherReference)






