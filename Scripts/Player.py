from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
from Scripts.Input import Input
from Scripts.Entity import Entity


class Player(Entity, Collidable):
    def __init__(self):
        Entity.__init__(self)
        self.loadImage("./resources/character.png")
        Collidable.__init__(self, box=Vector(self.width, self.height))
        self.jumpTime = 0
        self.jumping = True
        self.falling = True
        self.fallTime = 0

    # def move(self, deltaTime, moveDir): base entity function is good enough

    def update(self, deltaTime, gravity):
        self.updateCollidable(self.pos)
        if self.jumping:
            self._jump(deltaTime, gravity)
        else:
            self.jumpTime = 0

        self._fall(deltaTime, gravity)
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

        if Input.space and self.collisionInfo["Bottom"]:
            moveDir = moveDir + Vector(0, -1)
            self.jumping = True

        return moveDir.normalized()

    def _jump(self, deltaTime, gravity):
        if not self.falling:
            self.jumpTime += deltaTime
            self.pos.y -= 1 - gravity * self.jumpTime ** 2

        if self.collisionInfo["Bottom"]:
            self.jumpTime = 0
            self.jumping = False

    def _fall(self, deltaTime, gravity):
        if not self.collisionInfo["Bottom"] and not self.jumping:
            self.falling = True
            self.fallTime += deltaTime
            self.pos.y += gravity * self.fallTime ** 2
        else:
            self.fallTime = 0
            self.falling = False
