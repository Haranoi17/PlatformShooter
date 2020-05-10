from GameScripts.Vector import Vector


class Collidable:
    collidables = []

    def __init__(self):
        self.pos = Vector()
        self.box = Vector(30, 30)
        self.collisionInfo = {"Right": False, "Left": False, "Top": False, "Bottom": False}
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
        Collidable.collidables.append(self)

    def _updatePos(self, pos):
        self.pos = pos

    def _updateSides(self):
        self.left = self.pos.x - self.box.x
        self.right = self.pos.x + self.box.x
        self.top = self.pos.y + self.box.y
        self.bottom = self.pos.y - self.box.y

    # Checks if collision occured and sends information which side has collided
    def _collisionCheck(self, other):
        if ((other.left < self.right < other.right) or (
                other.left < self.left < other.right)) and (
                (other.bottom < self.top < other.top) or (
                other.bottom < self.bottom < other.top)):
            if other.left < self.right < other.right:
                self.collisionInfo["Right"] = True

            if other.left < self.left < other.right:
                self.collisionInfo["Left"] = True

            if other.top > self.top > other.bottom:
                self.collisionInfo["Bottom"] = True  # there is some bullshit... I've missed something
                #
            if other.top > self.bottom > other.bottom:  #
                self.collisionInfo["Top"] = True  #

    # public functions to use
    def updateCollidable(self, pos):
        self._updatePos(pos)
        self._updateSides()

    @classmethod
    # This method iterates through all collidable objects and check for collision
    def distributeCollisios(cls):
        for i in range(len(cls.collidables) - 1):
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
