from Scripts.Vector import Vector


class Collidable:
    collidables = []

    def __init__(self, pos=Vector(), box=Vector(30, 30)):
        self.pos = pos
        self.box = box
        self.collisionInfo = {"Right": False, "Left": False, "Top": False, "Bottom": False}
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
        Collidable.collidables.append(self)

    def __del__(self):
        Collidable.collidables.remove(self)

    def _updatePos(self, pos):
        self.pos = pos

    def _updateSides(self):
        self.left = self.pos.x - self.box.x/2
        self.right = self.pos.x + self.box.x/2
        self.top = self.pos.y - self.box.y/2
        self.bottom = self.pos.y + self.box.y/2

    # Checks if collision occured and sends information which side has collided
    def _collisionCheck(self, other):

        if ((other.left < self.right < other.right) or (other.left < self.left < other.right)) and (
                (other.bottom > self.top > other.top) or (other.bottom > self.bottom > other.top)):

            if other.top < self.bottom < other.bottom:
                self.collisionInfo["Bottom"] = True

            if other.bottom > self.top > other.top:
                self.collisionInfo["Top"] = True

            if other.left < self.right < other.right:
                self.collisionInfo["Right"] = True

            if other.left < self.left < other.right:
                self.collisionInfo["Left"] = True

    # public functions to use
    def updateCollidable(self, pos):
        self._updatePos(pos)
        self._updateSides()

    @classmethod
    # This method iterates through all collidable objects and check for collision
    def checkAllCollisions(cls):
        for i in range(len(cls.collidables)):
            for j in range(i + 1, len(cls.collidables)):
                cls.collidables[i]._collisionCheck(cls.collidables[j])

    @classmethod
    # This method prepares objects for next check
    def resetCollisions(cls):
        for item in cls.collidables:
            item.collisionInfo["Right"] = False
            item.collisionInfo["Left"] = False
            item.collisionInfo["Top"] = False
            item.collisionInfo["Bottom"] = False
