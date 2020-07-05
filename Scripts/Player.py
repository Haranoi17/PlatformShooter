from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
from Scripts.Input import Input
from Scripts.Entity import Entity


class Player(Entity, Collidable):
    def __init__(self):
        Entity.__init__(self)
        self.loadImage("./resources/character.png")
        Collidable.__init__(self, box=Vector(self.width, self.height))


    #def move(self, deltaTime, moveDir): base entity function is good enough

    def update(self, deltaTime):
        self.updateCollidable(self.pos)
        moveDir = self._calculateMoveDirection()
        self.move(deltaTime, moveDir)

    def _calculateMoveDirection(self):
        # Returns normalized move direction vector according to buttons pressed
        moveDir = Vector()

        if Input.left and not self.collisionInfo["Left"]:
            moveDir = moveDir + Vector(-1, 0)

        if Input.right and not self.collisionInfo["Right"]:
            moveDir = moveDir + Vector(1, 0)

        if Input.up and not self.collisionInfo["Top"]:
            moveDir = moveDir + Vector(0, -1)

        if Input.down and not self.collisionInfo["Bottom"]:
            moveDir = moveDir + Vector(0, 1)

        if Input.space:
            if not self.falling:
                self.jumping = True
        else:
            self.jumping = False

        return moveDir.normalized()
