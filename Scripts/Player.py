from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
from Scripts.Input import Input


class Player(Collidable):
    def __init__(self):
        self.speed = 1.0
        self.pos = Vector()
        self.jumping = False
        self.falling = True
        Collidable.__init__(self)

    def move(self, deltaTime):
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

        moveDir = moveDir.normalized()

        self.pos = self.pos + moveDir

    def update(self, deltaTime):
        self.updateCollidable(self.pos)
        self.move(deltaTime)
        # self.draw()
