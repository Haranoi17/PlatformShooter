from GameScripts.Vector import *
from GameScripts.CollisionSystem import *
from GameScripts.Input import *

class Player(Collidable):
    def __init__(self):
        self.speed = 1.0
        self.pos = Vector()
        self.jumping = False
        self.falling = True
        Collidable.__init__(self)

    def move(self, deltaTime):
        moveDir = Vector()

        if Input.left:
            moveDir = moveDir + Vector(-1, 0)

        if Input.right:
            moveDir = moveDir + Vector(1, 0)

        if Input.up:
            moveDir = moveDir + Vector(0, -1)

        if Input.down:
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
