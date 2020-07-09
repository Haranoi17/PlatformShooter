from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
from Scripts.Input import Input
from Scripts.Entity import Entity
from Scripts.Platform import Platform
from Scripts.Gun import Gun
from Scripts.Bullet import Bullet
from Scripts.Animation import Animation
import random
import math
import pygame



class Player(Entity, Collidable, Animation):
    def __init__(self):
        Entity.__init__(self)
        self.imageOffset = Vector(20, -20)
        Animation.__init__(self, "./resources/Animations/Knight/")
        self.width = self.getImageSize().x
        self.height = self.getImageSize().y
        Collidable.__init__(self, box=Vector(self.width-90, self.height-70))
        self.jumpTime = 0
        self.jumping = False
        self.falling = True
        self.rising = False
        self.standing = False
        self.fallTime = 0
        self.explicitMoveAllowed = True
        self.prevPos = self.pos
        self.gun = Gun()

    # def move(self, deltaTime, moveDir): base entity function is good enough

    def update(self, deltaTime, gravity):
        self.updateCollidable(self.pos)

        # prevPos has to be written after rising and falling
        self._jump(deltaTime, gravity)
        self._fall(deltaTime, gravity)
        self._isFalling()
        self._isRising()
        self.animate()
        if Input.mouseRight:
            self.changeCurrentAnimation(self.animationNames[random.randint(0, len(self.animationNames)-1)])
        self.prevPos = self.pos

        self._shoot()
        moveDir = self._calculateMoveDirection()
        self.move(deltaTime, moveDir)

    def _shoot(self):
        if Input.mouseLeft:
            self.gun.shoot(self.pos, self, self._calculateMouseRelativePosition())

    def _calculateMoveDirection(self):
        """Returns normalized move direction vector according to buttons pressed"""
        moveDir = Vector()

        if Input.left and self.explicitMoveAllowed:
            moveDir = moveDir + Vector(-1, 0)

        if Input.right and self.explicitMoveAllowed:
            moveDir = moveDir + Vector(1, 0)

        # if Input.up and not self.collisionInfo["Top"]:
        #     moveDir = moveDir + Vector(0, -1)

        # if Input.down and not self.collisionInfo["Bottom"]:
        #     moveDir = moveDir + Vector(0, 1)

        if Input.space and self.collisionInfo["Bottom"] and self.explicitMoveAllowed:
            moveDir = moveDir + Vector(0, -1)
            self.jumping = True

        return moveDir.normalized()

    def _calculateMouseRelativePosition(self):
        """Returns normalized direction from character towards mouse cursor"""
        mouse_x, mouse_y = pygame.mouse.get_pos()  # tuple (x, y)
        relativeMousePos = Vector(mouse_x - self.pos.x, mouse_y - self.pos.y)
        return relativeMousePos.normalized()

    def _jump(self, deltaTime, gravity):
        if self.jumping:
            self.explicitMoveAllowed = True
            self.jumpTime += deltaTime
            self.pos.y -= 2.5 - gravity * self.jumpTime ** 2

        #if self.collisionInfo["Bottom"] and not self.rising:
        #     self.jumpTime = 0
        #     self.jumping = False

    def _fall(self, deltaTime, gravity):
        if not self.collisionInfo["Bottom"]:
            self.explicitMoveAllowed = True
            self.fallTime += deltaTime
            self.pos.y += 0.5 + gravity * self.fallTime ** 2

    def _isRising(self):
        self.rising = True if self.prevPos.y > self.pos.y else False

    def _isFalling(self):
        self.falling = True if self.prevPos.y < self.pos.y else False

    def _collisionBehaviourDependingOnTypesOfObjects(self, other):
        if isinstance(other, Platform):
            self.explicitMoveAllowed = True
            if self.collisionInfo["Bottom"] and not self.rising:
                self.falling = False
                self.jumping = False
                self.fallTime = 0
                self.jumpTime = 0
                self.standing = True
            else:
                self.standing = False
        else:
            self.explicitMoveAllowed = False

        if isinstance(other, Bullet) and not other.playerImmune == self:
            self.getDamage(other.dmg)
            Bullet.remove(other)

